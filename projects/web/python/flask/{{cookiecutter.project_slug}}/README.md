# {{ cookiecutter.project_name }}

{% if cookiecutter.description %}{{ cookiecutter.description }}

{% endif %}## Run

```bash
poetry install --with dev,code-quality
poetry run flask --app app run --debug --port 8000    # http://localhost:8000/health
poetry run gunicorn --bind 0.0.0.0:8000 'app:create_app()'
```

The server listens on `$PORT` (`ap-build start` and the `Dockerfile` use it; default `8000`) — see `.env.example`.

```bash
docker build -t {{ cookiecutter.project_slug }} .
docker run --rm -p 8000:8000 {{ cookiecutter.project_slug }}
```

## Test / lint

```bash
poetry run pytest
poetry run ruff check .
poetry run ruff format --check .
```

## Layout

Four layers; each one depends only on the ones below it.

```
app/
├── __init__.py       create_app(), __version__
├── api/              HTTP only — blueprints, status codes, request parsing; no rules
│   ├── health.py       GET /health
│   └── v1/           versioned blueprints; items is the example resource
├── schemas/          the contract of every request and response
├── services/         business rules; receive repositories, raise DomainError
├── repositories/     data access — one class per store, one method per query
└── core/             cross-cutting: errors
tests/
├── support/          builders shared by every test (make_client)
├── api/              contract through Flask's test client
└── services/         rules, with a repository and no HTTP
```

`api` calls `services`, never a repository. `services` raise `DomainError` subclasses (`NotFoundError`, `ValidationError`, `ConflictError`); `core/errors.py` turns them, and Flask's own HTTP errors, into `{"detail": {"code", "message", "field"}}`: 404 for unknown ids and routes, 422 for invalid input. `repositories` hold no rules and no HTTP — the in-memory one behind `items` is the placeholder for a database or an external API.
