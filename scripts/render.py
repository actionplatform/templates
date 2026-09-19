"""Render every project template the way the platform does and check the result.

    python scripts/render.py --list            # the matrix: one line of JSON per template
    python scripts/render.py --ci github OUT   # render all into OUT/<id>/sample-app
    python scripts/render.py --ci gitlab --only web/python/fastapi OUT
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from cookiecutter.main import cookiecutter

ROOT = Path(__file__).resolve().parent.parent
INDEX = json.loads((ROOT / "index.json").read_text())
CI_FILES = {
    "github": [".github/workflows"],
    "gitlab": [".gitlab-ci.yml"],
    "jenkins": ["Jenkinsfile"],
    "bitbucket": ["bitbucket-pipelines.yml"],
}
LEFTOVER = re.compile(r"\{\{\s*cookiecutter\.|\{%")


def templates() -> list[dict]:
    dirs = {
        str(p.parent.relative_to(ROOT / "projects"))
        for p in (ROOT / "projects").rglob("cookiecutter.json")
    }
    ids = {p["id"] for p in INDEX["projects"]}

    if dirs != ids:
        sys.exit(f"index.json and projects/ disagree: {sorted(dirs ^ ids)}")

    return INDEX["projects"]


def render(template: dict, ci: str, out: Path) -> Path:
    target = out / template["id"]
    target.mkdir(parents=True, exist_ok=True)
    path = Path(
        cookiecutter(
            str(ROOT),
            directory=f"projects/{template['id']}",
            no_input=True,
            output_dir=str(target),
            overwrite_if_exists=True,
            extra_context={"project_name": "Sample App", "ci": ci},
        )
    )
    check(path, ci, template)

    return path


def check(project: Path, ci: str, template: dict) -> None:
    problems = []

    for file in project.rglob("*"):
        if file.is_file() and file.suffix not in {".png", ".ico", ".jar"}:
            try:
                text = file.read_text()
            except UnicodeDecodeError:
                continue

            if LEFTOVER.search(text):
                problems.append(f"unrendered cookiecutter tag in {file.relative_to(project)}")

    for provider, paths in CI_FILES.items():
        for rel in paths:
            exists = (project / rel).exists()

            if provider == ci and not exists and template["id"] != "empty":
                problems.append(f"{rel} missing for ci={ci}")

            if provider != ci and exists:
                problems.append(f"{rel} left behind for ci={ci}")

    if not (project / "platform.toml").exists():
        problems.append("platform.toml missing")

    if (project / "LAST_VERSION").read_text().strip() != "0.0.0":
        problems.append("LAST_VERSION is not 0.0.0")

    if problems:
        sys.exit(f"{template['id']}: " + "; ".join(problems))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--ci", default="github", choices=sorted(CI_FILES))
    parser.add_argument("--only")
    parser.add_argument("out", nargs="?", type=Path)
    args = parser.parse_args()

    if args.list:
        print(
            json.dumps(
                [
                    {"id": t["id"], "language": t["language"] or "none", "type": t["type"]}
                    for t in templates()
                ]
            )
        )
        return

    if args.out is None:
        parser.error("out is required")

    for template in templates():
        if args.only and template["id"] != args.only:
            continue

        path = render(template, args.ci, args.out)
        print(f"{template['id']}: {path}")


if __name__ == "__main__":
    main()
