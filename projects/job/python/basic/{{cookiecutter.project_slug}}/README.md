# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

A command that runs once and exits, started by a scheduler. It logs to stdout, reads its config from the environment and exits with `0` on success or `1` on a handled failure. No server stays running.

## Install

```bash
poetry install --with dev,code-quality
```

## Run

```bash
poetry run python -m app                              # hello, world
GREETING_NAME=Ada LOG_LEVEL=DEBUG poetry run python -m app
```

| Variable | Default | Effect |
|---|---|---|
| `LOG_LEVEL` | `INFO` | logging level |
| `GREETING_NAME` | `world` | who the example task greets; empty makes the job fail |

See `.env.example`.

## Test / lint

```bash
poetry run pytest
poetry run ruff check .
poetry run ruff format --check .
poetry run mypy --config-file .code_quality/mypy.ini .
```

## Schedule

`schedule/` holds examples; the command to run is `python -m app`.

- `schedule/Dockerfile` builds the image from the project root: `docker build -f schedule/Dockerfile -t {{ cookiecutter.project_slug }} .`
- `schedule/crontab` runs that image daily at 03:00 with `docker run --rm --env-file`. Install it with `crontab schedule/crontab` on a host with Docker.
- `schedule/Jenkinsfile` is a declarative pipeline with `cron('H 3 * * *')` that runs `python -m app` in a `python:{{ cookiecutter._python_version }}-slim` container. Point a Jenkins pipeline job at it.
- Dokploy: deploy the image as an application and add a schedule on it that runs `python -m app` in the application's container.

## Layout

```
app/
├── __init__.py      __version__
├── __main__.py      arguments, logging setup, exit code
└── task.py          the work: reads env, raises on failure
schedule/
├── Dockerfile
├── crontab
└── Jenkinsfile
tests/
└── test_job.py
```
