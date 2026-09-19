# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Install

```bash
pip install {{ cookiecutter.project_slug }}
```

## Usage

```python
from {{ cookiecutter.package_name }} import hello

hello("ana")  # "hello, ana"
```

## Develop

```bash
poetry install --with dev,code-quality
poetry run pytest
poetry run ruff check .
poetry run ruff format --check .
poetry run mypy --config-file .code_quality/mypy.ini .
```

## Layout

```
{{ cookiecutter.package_name }}/
├── __init__.py      # version + public API
└── hello.py         # hello() — dummy
tests/
```

## Publish

Releasing does not publish. The platform deploys a release to a scope — `testpypi` for candidates, `pypi` for stable releases — by dispatching `.github/workflows/publish.yml` on the tag with `version` and `registry`; the workflow builds and uploads with trusted publishing (register the repository as a trusted publisher on PyPI and TestPyPI once). `platform.toml` declares both targets.
