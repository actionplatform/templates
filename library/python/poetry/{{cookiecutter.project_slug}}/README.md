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
```

## Layout

```
{{ cookiecutter.package_name }}/
├── __init__.py      # version + public API
└── hello.py         # hello() — dummy
tests/
```
