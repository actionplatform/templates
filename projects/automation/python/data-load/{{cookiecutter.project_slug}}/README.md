# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

Each run reads `data/example.csv`, transforms the rows and upserts them into a `records` table in Postgres inside one transaction. Running it twice leaves the same rows: the second run reports `unchanged` for every row. Replace `data/example.csv` and `app/source.py` with your own source.

## Install

```bash
poetry install --with dev,code-quality
```

## Run

Set `DATABASE_URL` (see `.env.example`), then:

```bash
poetry run python -m app             # inserted=3 updated=0 unchanged=0
poetry run python -m app             # inserted=0 updated=0 unchanged=3
poetry run python -m app --dry-run   # same counts, transaction rolled back
```

Exit code is `0` on success and `1` when the source or the load fails.

## Test / lint

Unit tests need no database. The integration tests in `tests/test_load.py` run only when `DATABASE_URL` is set and drop and recreate the `records` table, so point them at a throwaway database.

```bash
poetry run pytest
poetry run ruff check .
poetry run ruff format --check .
poetry run mypy --config-file .code_quality/mypy.ini .
```

## Schedule

`schedule/` holds examples; the container's command is `python -m app`.

- `schedule/Dockerfile` builds the image from the project root: `docker build -f schedule/Dockerfile -t {{ cookiecutter.project_slug }} .`
- `schedule/crontab` runs that image daily at 03:00 with `docker run --env-file`, where the env file defines `DATABASE_URL`. Install it with `crontab schedule/crontab` on a host with Docker.
- `schedule/Jenkinsfile` is a separate pipeline for a scheduled Jenkins job: `cron('H 3 * * *')`, built from the same Dockerfile, with `DATABASE_URL` bound from the Jenkins credential `database-url` (a secret text credential you create).
- Dokploy: deploy the image as an application, set `DATABASE_URL` in its environment, and add a schedule on the application that runs `python -m app` in its container.

## Layout

```
app/
├── __init__.py      __version__
├── __main__.py      entrypoint: --dry-run; exit code
├── source.py        read the CSV, transform rows into records
└── load.py          create the table and upsert in one transaction
data/
└── example.csv      example source
schedule/
├── Dockerfile
├── crontab
└── Jenkinsfile
tests/
├── test_source.py   no database
└── test_load.py     needs DATABASE_URL
```
