# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

A shell for scripts, integrations and tasks run by hand or by an external system. No scheduler, no API, no database.

## Install

```bash
poetry install --with dev,code-quality
```

## Run

```bash
poetry run python -m app
poetry run python -m app --name Fernando     # hello, Fernando
```

Exit code is `0` on success and `1` when the task raises, so a caller (cron, CI, another program) can tell.

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
├── __main__.py      parses arguments, runs the task, prints the result
└── tasks/
    └── hello.py     a task: a plain function, arguments in, result out
tests/
└── test_hello.py
```

A new task is a new module under `app/tasks/` and a line in `__main__.py`; keep tasks free of printing and argument parsing so they stay testable.
