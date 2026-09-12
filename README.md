# Action Platform — Templates

Cookiecutter templates for bootstrapping projects on the Action Platform.

## Usage

```bash
pipx install cookiecutter

cookiecutter gh:actionplatform/templates --directory web/python/fastapi
```

Or via the CLI:

```bash
action-platform init                        # interactive: type → stack → template → name
action-platform init web python fastapi     # direct
action-platform init web python             # default template for the stack
action-platform init web python --cloud aws/lambda
action-platform init --list                 # projects and clouds
action-platform cloud set docker            # overlay on an existing project
```

## Projects

Under `projects/`, three levels: **type → stack → template**.

| Type      | Stacks                             |
|-----------|------------------------------------|
| `web`     | python (fastapi, fastmcp), go, node |
| `library` | python, go, php, node, java, rust  |
| `docs`    | mkdocs                             |
| `plugin`  | chrome                             |
| `empty`   | — (only `platform.toml` + `.code_quality/`) |

`plugin` stack is the **host system** — it imposes the language.

## Clouds

Under `cloud/`, deploy overlays applied **on top** of a generated project. Projects stay cloud-agnostic; the overlay adds only deploy files and sets `[deploy] target` in `platform.toml`.

| Cloud        | Types    | Languages        | Adds                                            |
|--------------|----------|------------------|-------------------------------------------------|
| `aws/lambda` | web      | python           | `template.yaml`, `samconfig.toml`, `lambda_handler.py`, `Makefile`, deploy workflow |
| `docker`     | web      | python, go, node | `Dockerfile`, `docker-compose.yml`, `.dockerignore` |
| `aws/amplify` | web     | node             | `amplify.yml`, `customHttp.yml`, deploy workflow (start job + wait) |

Language-specific files live in `_lang/<language>/`; the post-gen hook keeps the matching one.

AWS overlays ship `requirements/` — `trust.json` (GitHub OIDC for the repo) and `policy.json` (least privilege the deploy role needs). `DEPLOY.md` shows the two `aws iam` commands to create the role.

Convention: every `web/python/*` template exposes `app.create_app()` — the Lambda handler, uvicorn and tests build the app through it. MCP servers are `web` too (`web/python/fastmcp`).

## Services

Under `service/`, application dependencies. Each adds `services/<name>/` to the project with an `up` script (provision), a `link` script (prints env vars) and the provider's files. Pick the provider with `provider=`.

| Service    | Providers        | Exposes |
|------------|------------------|---------|
| `postgres` | docker, aws-rds  | `DATABASE_URL` |

```bash
action-platform service add postgres --provider docker
eval "$(./services/postgres/link)"
```

## Structure

```
templates/
├── index.toml                        # matrix read by the CLI
├── projects/
│   ├── web/python/fastapi/
│   ├── web/go/gin/
│   ├── web/node/react/
│   ├── library/python/poetry/
│   ├── web/python/fastmcp/
│   ├── docs/mkdocs/material/
│   ├── plugin/chrome/vanilla/
│   └── empty/
├── cloud/
│   ├── aws/lambda/
│   ├── aws/amplify/
│   └── docker/
└── service/
    └── postgres/
```

Each leaf is an independent cookiecutter template with its own `cookiecutter.json`. Select it with `--directory projects/<type>/<stack>/<template>` or `--directory cloud/<name>`.

## `index.toml`

```toml
[project.web.python.fastapi]
default = true
description = "FastAPI + uvicorn + pydantic"

[cloud.aws.lambda]
description = "AWS Lambda + HTTP API Gateway via SAM"
languages = ["python"]
types = ["web"]
```

## CI

Every template (except `empty`) ships config for three CI providers. Pick one with the `ci` variable; the post-gen hook removes the others.

| `ci`        | File                          |
|-------------|-------------------------------|
| `github`    | `.github/workflows/code-quality.yml` |
| `gitlab`    | `.gitlab-ci.yml`              |
| `jenkins`   | `Jenkinsfile`                 |

```bash
cookiecutter gh:actionplatform/templates --directory web/python/fastapi ci=gitlab
```

All three call the same scripts from [ci-scripts](https://github.com/actionplatform/ci-scripts) through [ci-github](https://github.com/actionplatform/ci-github) (composite actions), [ci-gitlab](https://github.com/actionplatform/ci-gitlab) (`include: remote`) and [ci-jenkins](https://github.com/actionplatform/ci-jenkins) (shared library).

## Conventions

- Every template ships `platform.toml` so the project works with `action-platform release` and `deploy` out of the box.
- Every template ships `.code_quality/` with the stack's lint/format config.
- Each stack has exactly one template with `default = true`.
- Variables are declared in `cookiecutter.json`; keep defaults sensible.

## Related

- [action-platform](https://github.com/actionplatform/action-platform) — CLI and core
- [strategy](https://github.com/actionplatform/strategy) — vision and decisions
