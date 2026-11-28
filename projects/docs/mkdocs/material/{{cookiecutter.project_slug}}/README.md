# {{ cookiecutter.project_name }}

{% if cookiecutter.description %}{{ cookiecutter.description }}

{% endif %}Documentation site built with MkDocs Material.

```bash
poetry install
poetry run mkdocs serve             # http://127.0.0.1:8000
poetry run mkdocs build --strict    # what CI runs
```

Pages live in `docs/`; navigation in `mkdocs.yml`.
