# {{ cookiecutter.project_name }}

{% if cookiecutter.description %}{{ cookiecutter.description }}

{% endif %}## Run

```bash
poetry install --with dev,code-quality
poetry run python manage.py runserver    # http://localhost:8000/health
poetry run gunicorn --bind 0.0.0.0:8000 app.wsgi:application
```

The server listens on `$PORT` (`ap-build start` and the `Dockerfile` use it; default `8000`). `DEBUG`, `SECRET_KEY` and `ALLOWED_HOSTS` are read from the environment — see `.env.example`; with no `SECRET_KEY` a random one is made at start.

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

```
app/
├── __init__.py       create_app() → WSGI application, __version__
├── settings.py       from the environment; no database
├── urls.py           /health and /api/v1
├── health.py         GET /health
├── wsgi.py           gunicorn app.wsgi:application
├── core/errors.py    DomainError → {"detail": {"code", "message", "field"}}
└── items/            the example resource: /api/v1/items
    ├── views.py        HTTP only — parse, call the service, serialize
    ├── serializers.py  DRF — the contract of every request and response
    ├── services.py     business rules; raise DomainError subclasses
    ├── repositories.py data access — the in-memory one is the placeholder for a database
    └── models.py       plain dataclasses
tests/
├── support/          builders shared by every test (make_client)
├── api/              contract through DRF's APIClient
└── services/         rules, with a repository and no HTTP
```

`views` call `services`, never a repository. `services` raise `DomainError` subclasses (`NotFoundError`, `ValidationError`, `ConflictError`); `core/errors.py` turns them, and DRF's own errors, into one shape: `{"detail": {"code", "message", "field"}}` with 404 for unknown ids and routes and 422 for invalid input.
