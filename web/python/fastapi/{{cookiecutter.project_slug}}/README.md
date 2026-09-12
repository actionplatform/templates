# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Run

```bash
poetry install --with dev,code-quality
poetry run uvicorn app:app --reload    # http://localhost:8000/docs
```

Settings come from env vars (`SCOPE`, `API_V1_PREFIX`, `CORS_ORIGINS`, `SECRET_KEY`) or a local `.env`.

## Test / lint

```bash
poetry run pytest
poetry run ruff check .
poetry run ruff format --check .
```

## Layout

```
app/
├── __init__.py        # create_app()
├── settings.py        # pydantic settings
└── api/
    ├── ping.py        # liveness
    └── v1/            # versioned routers
lambda_handler.py      # Mangum adapter for AWS Lambda
```
