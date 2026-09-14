# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

Jobs that an external scheduler runs — cron, GitHub Actions, EventBridge, a Kubernetes CronJob. Nothing stays resident: each invocation runs one job and exits.

## Install

```bash
poetry install --with dev,code-quality
```

## Run

```bash
poetry run python -m app list             # example
poetry run python -m app run example      # example ran at 2026-01-01T00:00:00+00:00
```

Exit code is `0` on success and `1` when the job raises or does not exist. A crontab line:

```
0 * * * * cd /srv/{{ cookiecutter.project_slug }} && poetry run python -m app run example
```

## Test / lint

```bash
poetry run pytest
poetry run ruff check .
poetry run ruff format --check .
poetry run mypy .
```

## Layout

```
app/
├── __init__.py      __version__
├── __main__.py      list · run <job>
├── scheduler.py     the registry: name → job
└── jobs/
    └── example.py   a job: run() -> str, raises on failure
tests/
└── test_example_job.py
```

A new job is a module under `app/jobs/` with `run()` and one line in `scheduler.JOBS`.
