# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Install

```bash
pipx install {{ cookiecutter.project_slug }}      # from PyPI, once published
poetry install --with dev,code-quality         # for development
```

## Run

```bash
poetry run {{ cookiecutter.project_slug }} version
poetry run {{ cookiecutter.project_slug }} hello
poetry run {{ cookiecutter.project_slug }} hello --name Fernando
python -m {{ cookiecutter.package_name }} hello
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
{{ cookiecutter.package_name }}/
├── __init__.py      __version__
├── __main__.py      python -m {{ cookiecutter.package_name }}
└── cli.py           the Typer app and its commands (version, hello)
tests/
└── test_cli.py      CliRunner
```

A new command is a function decorated with `@app.command()` in `cli.py`; keep the body small and call plain functions.
