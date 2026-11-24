"""Check the Claude Code and Codex plugin manifests under a root."""

import json
import sys
from pathlib import Path

CLAUDE_PLUGIN = ".claude-plugin/plugin.json"
CLAUDE_MARKETPLACE = ".claude-plugin/marketplace.json"
CODEX_PLUGIN = ".codex-plugin/plugin.json"
CODEX_MARKETPLACE = ".agents/plugins/marketplace.json"
MCP_CONFIG = ".mcp.json"
SKILL_FILE = "SKILL.md"


def load(root: Path, rel: str, problems: list[str]) -> dict | None:
    path = root / rel
    if not path.is_file():
        problems.append(f"{rel}: missing file")
        return None
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as error:
        problems.append(f"{rel}: invalid JSON ({error})")
        return None
    if not isinstance(data, dict):
        problems.append(f"{rel}: expected a JSON object")
        return None
    return data


def frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        key, separator, value = line.partition(":")
        if separator and value.strip():
            fields[key.strip()] = value.strip()
    return {}


def check_skill(skill_dir: Path, root: Path, problems: list[str]) -> None:
    rel = (skill_dir / SKILL_FILE).relative_to(root).as_posix()
    path = skill_dir / SKILL_FILE
    if not path.is_file():
        problems.append(f"{rel}: missing file")
        return
    fields = frontmatter(path.read_text())
    for key in ("name", "description"):
        if key not in fields:
            problems.append(f"{rel}: frontmatter lacks {key}")
    if "name" in fields and fields["name"] != skill_dir.name:
        problems.append(
            f"{rel}: name {fields['name']!r} differs from folder"
            f" {skill_dir.name!r}"
        )


def check_skills(
    root: Path, rel: str, manifest: dict, problems: list[str]
) -> None:
    value = manifest.get("skills")
    if not isinstance(value, str):
        problems.append(f"{rel}: skills path missing")
        return
    skills = root / value
    if not skills.is_dir():
        problems.append(f"{rel}: skills path {value} does not exist")
        return
    for skill_dir in sorted(p for p in skills.iterdir() if p.is_dir()):
        check_skill(skill_dir, root, problems)


def check(root: Path) -> list[str]:
    problems: list[str] = []
    claude = load(root, CLAUDE_PLUGIN, problems)
    codex = load(root, CODEX_PLUGIN, problems)
    load(root, CLAUDE_MARKETPLACE, problems)
    load(root, CODEX_MARKETPLACE, problems)
    load(root, MCP_CONFIG, problems)

    if claude is not None:
        check_skills(root, CLAUDE_PLUGIN, claude, problems)
    if codex is not None:
        check_skills(root, CODEX_PLUGIN, codex, problems)
    if claude is not None and codex is not None:
        left, right = claude.get("version"), codex.get("version")
        if left is None or right is None or left != right:
            problems.append(
                f"version mismatch: {CLAUDE_PLUGIN} has {left!r},"
                f" {CODEX_PLUGIN} has {right!r}"
            )
    return problems


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    root = Path(args[0]) if args else Path(__file__).resolve().parent.parent
    problems = check(root)
    for problem in problems:
        print(problem, file=sys.stderr)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
