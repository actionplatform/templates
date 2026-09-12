# Action Platform — Templates

Cookiecutter templates for bootstrapping projects on the Action Platform.

## Usage

```bash
pipx install cookiecutter

cookiecutter gh:actionplatform/templates --directory web/python/fastapi
cookiecutter gh:actionplatform/templates --directory plugin/wordpress/classic
```

Or via the CLI:

```bash
action-platform init                        # interactive: type → stack → template → name
action-platform init web python fastapi     # direct
action-platform init web python             # default template for the stack
action-platform init --list                 # show available matrix
```

## Matrix

Three levels: **type → stack → template**.

| Type      | Stacks                             |
|-----------|------------------------------------|
| `web`     | python, go, php, java, node, rust  |
| `library` | python, go, php, node, java, rust  |
| `mcp`     | python, go, node, java             |
| `mobile`  | android, ios                       |
| `docs`    | mkdocs, docusaurus                 |
| `plugin`  | wordpress, chrome                  |
| `empty`   | — (only `platform.toml` + `.code_quality/`) |

`plugin` stack is the **host system**; `mobile` stack is the **platform**. Language is imposed by them.

## Structure

```
templates/
├── index.toml                 # matrix read by the CLI
├── web/python/fastapi/
├── web/python/django/
├── web/go/gin/
├── library/python/poetry/
├── mcp/python/fastmcp/
├── mobile/android/compose/
├── plugin/wordpress/classic/
├── plugin/chrome/mv3/
└── empty/
```

Each leaf is an independent cookiecutter template with its own `cookiecutter.json`. Select it with `--directory <type>/<stack>/<template>`.

## `index.toml`

```toml
[web.python.fastapi]
default = true
description = "FastAPI + uvicorn + pydantic"

[web.python.django]
description = "Django + gunicorn"
```

## CI

Every template (except `empty`) ships config for four CI providers. Pick one with the `ci` variable; the post-gen hook removes the others.

| `ci`        | File                          |
|-------------|-------------------------------|
| `github`    | `.github/workflows/code-quality.yml` |
| `gitlab`    | `.gitlab-ci.yml`              |
| `bitbucket` | `bitbucket-pipelines.yml`     |
| `jenkins`   | `Jenkinsfile`                 |

```bash
cookiecutter gh:actionplatform/templates --directory web/python/fastapi ci=gitlab
```

All four run the same lint/format step for the stack (ruff, gofmt, eslint, phpcs, ...).

## Conventions

- Every template ships `platform.toml` so the project works with `action-platform release` and `deploy` out of the box.
- Every template ships `.code_quality/` with the stack's lint/format config.
- Each stack has exactly one template with `default = true`.
- Variables are declared in `cookiecutter.json`; keep defaults sensible.

## Related

- [action-platform](https://github.com/actionplatform/action-platform) — CLI and core
- [strategy](https://github.com/actionplatform/strategy) — vision and decisions
