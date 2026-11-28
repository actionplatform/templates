# {{ cookiecutter.project_name }}

{% if cookiecutter.description %}{{ cookiecutter.description }}

{% endif %}## Run

```bash
poetry install --with dev,code-quality
poetry run uvicorn app:app --reload    # http://localhost:8000/graphql
```

```bash
docker build -t {{ cookiecutter.project_slug }} .
docker run --rm -p 8000:8000 {{ cookiecutter.project_slug }}
curl localhost:8000/health
```

```graphql
mutation { createItem(input: {name: "pen"}) { id name } }
query { items { id name } }
query { item(id: 1) { id name } }
```

## Test / lint

```bash
poetry run pytest
poetry run ruff check .
poetry run ruff format --check .
poetry run mypy --config-file .code_quality/mypy.ini .
```

## Layout

Each layer depends only on the ones below it.

```
app/
├── __init__.py       create_app(), __version__
├── api/              GET /health
├── gql/              Strawberry types, Query, Mutation, schema; no rules
├── services/         business rules; receive repositories, raise DomainError
├── repositories/     data access, one class per store, one method per query
└── core/             cross-cutting: errors
tests/
├── support/          builders shared by every test (make_client, graphql)
├── api/              health through TestClient
├── gql/              queries and mutations through /graphql
└── services/         rules, with a repository and no GraphQL
```

`gql` calls `services`, never a repository. `services` raise `DomainError` subclasses (`NotFoundError`, `ValidationError`, `ConflictError`); `gql/errors.py` turns them into GraphQL errors with `extensions {"code", "field"}`. The in-memory repository behind `items` is the placeholder for a database or an external API.
