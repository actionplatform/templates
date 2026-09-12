# Action Platform — Templates

Cookiecutter templates for bootstrapping projects on the Action Platform.

## Usage

```bash
pipx install cookiecutter

cookiecutter gh:actionplatform/templates --directory python
cookiecutter gh:actionplatform/templates --directory node
```

Or via the CLI:

```bash
action-platform init python
```

## Structure

```
templates/
├── python/
│   ├── cookiecutter.json
│   └── {{cookiecutter.project_slug}}/
├── node/
│   ├── cookiecutter.json
│   └── {{cookiecutter.project_slug}}/
└── go/
    ├── cookiecutter.json
    └── {{cookiecutter.project_slug}}/
```

Each top-level directory is an independent cookiecutter template. Select it with `--directory <name>`.

## Conventions

- Every template ships `platform.toml` so the project works with `action-platform release` and `deploy` out of the box.
- Every template ships `.code_quality/` with the stack's lint/format config.
- Variables are declared in `cookiecutter.json`; keep defaults sensible.

## Related

- [action-platform](https://github.com/actionplatform/action-platform) — CLI and core
- [strategy](https://github.com/actionplatform/strategy) — vision and decisions
