import json
import shutil
from pathlib import Path

import pytest

from scripts.check_manifests import check, main

REAL_ROOT = Path(__file__).resolve().parent.parent
TRACKED = [
    ".claude-plugin",
    ".codex-plugin",
    ".agents",
    ".mcp.json",
    "skills",
]


@pytest.fixture
def root(tmp_path: Path) -> Path:
    for name in TRACKED:
        source = REAL_ROOT / name
        if source.is_dir():
            shutil.copytree(source, tmp_path / name)
        else:
            shutil.copy(source, tmp_path / name)
    return tmp_path


def rewrite(path: Path, **changes: object) -> None:
    data = json.loads(path.read_text())
    data.update(changes)
    path.write_text(json.dumps(data))


def test_real_project_is_consistent():
    assert check(REAL_ROOT) == []
    assert main([str(REAL_ROOT)]) == 0


def test_copy_is_consistent(root):
    assert check(root) == []


def test_invalid_json(root):
    (root / ".claude-plugin" / "plugin.json").write_text("{")
    assert any("invalid JSON" in p for p in check(root))


def test_missing_file(root):
    (root / ".mcp.json").unlink()
    assert ".mcp.json: missing file" in check(root)


def test_missing_skills_path(root):
    rewrite(root / ".codex-plugin" / "plugin.json", skills="./nope/")
    assert any("does not exist" in p for p in check(root))


def test_skill_without_frontmatter(root):
    (root / "skills" / "conventional-commit" / "SKILL.md").write_text("body")
    problems = check(root)
    assert any("lacks name" in p for p in problems)
    assert any("lacks description" in p for p in problems)


def test_skill_name_differs_from_folder(root):
    path = root / "skills" / "conventional-commit" / "SKILL.md"
    path.write_text(path.read_text().replace("name: conv", "name: other-conv"))
    assert any("differs from folder" in p for p in check(root))


def test_skill_folder_without_skill_file(root):
    (root / "skills" / "empty").mkdir()
    assert "skills/empty/SKILL.md: missing file" in check(root)


def test_version_mismatch(root):
    rewrite(root / ".codex-plugin" / "plugin.json", version="1.0.0")
    assert any("version mismatch" in p for p in check(root))


def test_main_lists_problems_and_exits_one(root, capsys):
    (root / ".mcp.json").unlink()
    assert main([str(root)]) == 1
    assert ".mcp.json: missing file" in capsys.readouterr().err
