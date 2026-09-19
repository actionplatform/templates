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
poetry run mypy --config-file .code_quality/mypy.ini .
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

## Publish

Releasing does not publish. The platform deploys a release to a scope by dispatching `.github/workflows/publish.yml` on the tag; a scope of criticality `test` publishes to TestPyPI, any other to PyPI. The workflow uploads with trusted publishing — register the repository as a trusted publisher on PyPI and TestPyPI once. `platform.toml` declares the target.
