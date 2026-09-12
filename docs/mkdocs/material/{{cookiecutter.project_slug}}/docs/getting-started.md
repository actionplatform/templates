# Getting started

## Run locally

```bash
poetry install
poetry run mkdocs serve      # http://127.0.0.1:8000
```

## Write

One topic per page under `docs/`. Add it to `nav` in `mkdocs.yml`. `mkdocs build --strict` fails on broken links — CI runs it.
