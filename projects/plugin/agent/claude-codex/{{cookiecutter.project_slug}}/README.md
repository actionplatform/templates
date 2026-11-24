# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

A plugin for Claude Code and Codex. One `skills/` folder serves both: each tool has its own manifest that points at it.

## Install

```bash
poetry install --with dev,code-quality
```

## Run

Claude Code, loading the plugin from this folder:

```bash
claude --plugin-dir .
```

Or through the marketplace in `.claude-plugin/marketplace.json`, inside Claude Code:

```
/plugin marketplace add ./
/plugin install {{ cookiecutter.project_slug }}@{{ cookiecutter.project_slug }}
```

Codex reads `.agents/plugins/marketplace.json` and `.codex-plugin/plugin.json`: add this folder as a local marketplace, then install `{{ cookiecutter.project_slug }}` from it.

The example skill is `conventional-commit`: it writes a Conventional Commits message for the staged diff.

`.mcp.json` declares one HTTP MCP server at `http://localhost:8000/mcp`. No server ships with this project: point the entry at your own, or delete the file together with its check in `scripts/check_manifests.py`.

## Test

```bash
poetry run python -m scripts.check_manifests
poetry run pytest
poetry run ruff check .
poetry run ruff format --check .
poetry run mypy --config-file .code_quality/mypy.ini .
```

`check_manifests` exits `1` and lists the problems when a manifest is missing or is not valid JSON, a `skills` path does not exist, a `SKILL.md` lacks `name` or `description` or its `name` differs from its folder, or the version in `.claude-plugin/plugin.json` differs from the one in `.codex-plugin/plugin.json`. The test suite runs it on this project, so CI fails when the manifests drift.

## Layout

```
.claude-plugin/
├── plugin.json         Claude Code manifest
└── marketplace.json    Claude Code marketplace, one plugin at ./
.codex-plugin/
└── plugin.json         Codex manifest
.agents/plugins/
└── marketplace.json    Codex marketplace, one local plugin at ./
.mcp.json               MCP server entry
skills/
└── conventional-commit/
    └── SKILL.md        name and description in the frontmatter, then the steps
scripts/
└── check_manifests.py
tests/
└── test_check_manifests.py
```

A new skill is a new folder under `skills/` with a `SKILL.md`; the folder name is the skill name.

## Versions

Both `plugin.json` files carry the version and must match; the checker fails when they differ. Change them together by hand.
