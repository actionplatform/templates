"""The files every project template shares, written from `projects/_shared/` into each template.

    python scripts/shared.py --write   # copy _shared into every template
    python scripts/shared.py --check   # exit 1 when a template drifted from _shared

Shared: the four GitHub workflows and `dependabot.yml` (`__ECOSYSTEM__` becomes the language's
package ecosystem), `.gitlab-ci.yml`, `Jenkinsfile` and `bitbucket-pipelines.yml` (`__IMAGE__`
becomes the language's CI image), the post-generation hook, `.editorconfig`, `LICENSE`,
`.gitignore` (`gitignore/common` + `gitignore/<language>`), and the head of `AGENTS.md` —
everything from `## Commits` to before `## Layout`, which each template writes itself.
The `empty` template gets `.editorconfig` and the common `.gitignore` only."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED = ROOT / "projects" / "_shared"
SLUG = "{{cookiecutter.project_slug}}"

IMAGES = {
    "python": "python:{{ cookiecutter._python_version }}",
    "node": "node:{{ cookiecutter._node_version }}",
    "go": "golang:{{ cookiecutter._go_version }}",
    "java": "maven:3-eclipse-temurin-{{ cookiecutter._java_version }}",
    "ruby": "ruby:{{ cookiecutter._ruby_version }}",
    "php": "composer:2",
    "rust": "rust:{{ cookiecutter._rust_version }}",
}

ECOSYSTEMS = {
    "python": "pip",
    "node": "npm",
    "go": "gomod",
    "java": "maven",
    "ruby": "bundler",
    "php": "composer",
    "rust": "cargo",
}

CI_FILES = [
    ".github/workflows/code-quality.yml",
    ".github/workflows/conventional-commit.yml",
    ".github/workflows/gitflow.yml",
    ".github/workflows/trivy.yml",
    ".github/dependabot.yml",
    ".gitlab-ci.yml",
    "Jenkinsfile",
    "bitbucket-pipelines.yml",
]
HOOK = "hooks/post_gen_project.py"
AGENTS_HEAD_START = "## Commits"
AGENTS_HEAD_END = "## Layout"


def templates() -> list[Path]:
    return sorted(
        p.parent
        for p in (ROOT / "projects").rglob("cookiecutter.json")
        if (p.parent / SLUG / "platform.toml").exists()
    )


def expected(template: Path) -> dict[Path, str]:
    language = json.loads((template / "cookiecutter.json").read_text()).get("_language")
    files = {template / SLUG / ".editorconfig": (SHARED / ".editorconfig").read_text()}
    gitignore = (SHARED / "gitignore" / "common").read_text()

    if not language:
        files[template / SLUG / ".gitignore"] = gitignore

        return files

    files[template / SLUG / ".gitignore"] = gitignore + (SHARED / "gitignore" / language).read_text()
    files[template / SLUG / "LICENSE"] = (SHARED / "LICENSE").read_text()

    for rel in CI_FILES:
        text = (
            (SHARED / rel)
            .read_text()
            .replace("__IMAGE__", IMAGES[language])
            .replace("__ECOSYSTEM__", ECOSYSTEMS[language])
        )
        files[template / SLUG / rel] = text

    files[template / HOOK] = (SHARED / HOOK).read_text()

    agents = template / SLUG / "AGENTS.md"

    if agents.exists():
        files[agents] = with_head(agents.read_text(), (SHARED / "AGENTS.md").read_text())

    return files


def with_head(current: str, head: str) -> str:
    start = current.find(AGENTS_HEAD_START)
    end = current.find(AGENTS_HEAD_END)

    if start < 0 or end < 0 or end < start:
        sys.exit(f"AGENTS.md needs a '{AGENTS_HEAD_START}' section followed by '{AGENTS_HEAD_END}'")

    return current[:start] + head + current[end:]


def main() -> None:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    drift = []

    for template in templates():
        for path, text in expected(template).items():
            if path.exists() and path.read_text() == text:
                continue

            drift.append(str(path.relative_to(ROOT)))

            if args.write:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text)

    if args.check and drift:
        sys.exit("drifted from projects/_shared (run scripts/shared.py --write):\n  " + "\n  ".join(drift))

    print(f"{len(drift)} file(s) {'written' if args.write else 'in sync'}" if args.write or not drift else "")


if __name__ == "__main__":
    main()
