# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Install

```bash
pip install {{ cookiecutter.project_slug }}
```

## Develop

```bash
poetry install --with dev,code-quality
poetry run pytest
poetry run ruff check .
```

## Layout

```
{{ cookiecutter.package_name }}/
└── __init__.py      # version + public API
tests/
```
