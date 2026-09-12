# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Run

```bash
poetry install --with dev,code-quality
poetry run uvicorn app:app --reload    # http://localhost:8000/docs
```

## Test / lint

```bash
poetry run pytest
poetry run ruff check .
poetry run ruff format --check .
```

## Layout

```
app/
├── __init__.py        # create_app(), __version__
└── api/
    ├── ping.py        # GET /ping
    └── v1/            # versioned routers (hello = dummy)
lambda_handler.py      # Mangum adapter for AWS Lambda
```
