# Action Platform — Templates

Cookiecutter templates for bootstrapping projects on the Action Platform.

## Usage

```bash
pipx install cookiecutter

cookiecutter gh:actionplatform/templates --directory projects/web/python/fastapi
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

| Type | Language | Framework | Template | Description | Default |
|---|---|---|---|---|:---:|
| `web` | <img src="assets/icons/python.svg" width="18" height="18" alt="python"> python | <img src="assets/icons/fastapi.svg" width="18" height="18" alt="fastapi"> FastAPI | `fastapi` | FastAPI + uvicorn + pydantic | ✓ |
|  | <img src="assets/icons/python.svg" width="18" height="18" alt="python"> python | <img src="assets/icons/mcp.svg" width="18" height="18" alt="mcp"> FastMCP | `fastmcp` | MCP server over HTTP |  |
|  | <img src="assets/icons/go.svg" width="18" height="18" alt="go"> go | <img src="assets/icons/gin.svg" width="18" height="18" alt="gin"> Gin | `gin` | Gin + net/http | ✓ |
|  | <img src="assets/icons/nodejs.svg" width="18" height="18" alt="nodejs"> node | <img src="assets/icons/react.svg" width="18" height="18" alt="react"> React | `react` | React + webpack + jest | ✓ |
|  | <img src="assets/icons/nodejs.svg" width="18" height="18" alt="nodejs"> node | <img src="assets/icons/fastify.svg" width="18" height="18" alt="fastify"> Fastify | `fastify` | Fastify + TypeScript + Vitest |  |
|  | <img src="assets/icons/nodejs.svg" width="18" height="18" alt="nodejs"> node | <img src="assets/icons/vite.svg" width="18" height="18" alt="vite"> React + Vite | `react-vite` | React + TypeScript + Vite + Vitest |  |
|  | <img src="assets/icons/java.svg" width="18" height="18" alt="java"> java | <img src="assets/icons/spring.svg" width="18" height="18" alt="spring"> Spring Boot | `spring` | Spring Boot web API (Maven, JDK 17) | ✓ |
|  | <img src="assets/icons/kotlin.svg" width="18" height="18" alt="kotlin"> kotlin | <img src="assets/icons/spring.svg" width="18" height="18" alt="spring"> Spring Boot | `spring` | Spring Boot web API in Kotlin (Maven, JDK 17) | ✓ |
| `library` | <img src="assets/icons/python.svg" width="18" height="18" alt="python"> python | <img src="assets/icons/poetry.svg" width="18" height="18" alt="poetry"> Poetry | `poetry` | Poetry package | ✓ |
|  | <img src="assets/icons/python.svg" width="18" height="18" alt="python"> python | <img src="assets/icons/python.svg" width="18" height="18" alt="python"> Typer | `typer` | Python CLI with Typer |  |
|  | <img src="assets/icons/go.svg" width="18" height="18" alt="go"> go | <img src="assets/icons/go.svg" width="18" height="18" alt="go"> Go module | `module` | Go module | ✓ |
|  | <img src="assets/icons/go.svg" width="18" height="18" alt="go"> go | <img src="assets/icons/go.svg" width="18" height="18" alt="go"> Cobra | `cobra` | Go CLI with Cobra |  |
|  | <img src="assets/icons/nodejs.svg" width="18" height="18" alt="nodejs"> node | <img src="assets/icons/npm.svg" width="18" height="18" alt="npm"> npm | `npm` | npm package + TypeScript | ✓ |
|  | <img src="assets/icons/php.svg" width="18" height="18" alt="php"> php | <img src="assets/icons/composer.svg" width="18" height="18" alt="composer"> Composer | `composer` | Composer package | ✓ |
|  | <img src="assets/icons/java.svg" width="18" height="18" alt="java"> java | <img src="assets/icons/maven.svg" width="18" height="18" alt="maven"> Maven | `maven` | Maven artifact | ✓ |
|  | <img src="assets/icons/rust.svg" width="18" height="18" alt="rust"> rust | <img src="assets/icons/rust.svg" width="18" height="18" alt="rust"> Cargo | `cargo` | Cargo crate | ✓ |
| `automation` | <img src="assets/icons/python.svg" width="18" height="18" alt="python"> python | <img src="assets/icons/python.svg" width="18" height="18" alt="python"> argparse | `basic` | Simple Python automation: `python -m app` | ✓ |
|  | <img src="assets/icons/python.svg" width="18" height="18" alt="python"> python | <img src="assets/icons/python.svg" width="18" height="18" alt="python"> argparse | `scheduled` | Scheduled Python jobs: `python -m app run <job>` |  |
| `docs` | mkdocs | <img src="assets/icons/mkdocs.svg" width="18" height="18" alt="mkdocs"> MkDocs Material | `material` | MkDocs Material site | ✓ |
| `plugin` | chrome | <img src="assets/icons/chrome.svg" width="18" height="18" alt="chrome"> Manifest V3 | `vanilla` | Chrome extension, no bundler | ✓ |
| `empty` | — | — | — | Only `platform.toml` + `.code_quality/` |  |

`action-platform init <type> <stack>` picks the default template of the pair; name the third part to pick another (`init web node fastify`). `plugin` stack is the **host system** — it imposes the language.

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

Every template (except `empty`) ships config for four CI providers. Pick one with the `ci` variable; the post-gen hook removes the others.

| `ci`        | File                          |
|-------------|-------------------------------|
| `github`    | `.github/workflows/code-quality.yml` |
| `gitlab`    | `.gitlab-ci.yml`              |
| `jenkins`   | `Jenkinsfile`                 |
| `bitbucket` | `bitbucket-pipelines.yml`     |

```bash
cookiecutter gh:actionplatform/templates --directory projects/web/python/fastapi ci=gitlab
```

All four call the same scripts from [ci-scripts](https://github.com/actionplatform/ci-scripts) through [ci-github](https://github.com/actionplatform/ci-github) (composite actions), [ci-gitlab](https://github.com/actionplatform/ci-gitlab) (`include: remote`), [ci-jenkins](https://github.com/actionplatform/ci-jenkins) (shared library) and [ci-bitbucket](https://github.com/actionplatform/ci-bitbucket) (a self-contained `bitbucket-pipelines.yml`, since Pipelines cannot include a remote file).

## Conventions

- Every template ships `platform.toml` so the project works with `action-platform release` and `deploy` out of the box.
- Every template ships `.code_quality/` with the stack's lint/format config.
- Git-flow and Conventional Commits are enforced by git hooks the CLI installs into `.git/hooks` (`action-platform install`, once per clone; `init`, `branch` and `push` do it too) and by the `gitflow` CI check on pull requests. Hooks are not versioned in the project.
- Each stack has exactly one template with `default = true`.
- Variables are declared in `cookiecutter.json`; keep defaults sensible.

## Related

- [action-platform](https://github.com/actionplatform/action-platform) — CLI and core
- [strategy](https://github.com/actionplatform/strategy) — vision and decisions
