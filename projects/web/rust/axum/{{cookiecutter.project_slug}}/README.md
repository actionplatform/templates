# {{ cookiecutter.project_name }}

{% if cookiecutter.description %}{{ cookiecutter.description }}

{% endif %}## Run

```bash
cargo run        # http://localhost:8000/health
```

`PORT` overrides the listen port (default `8000`) — the platform sets it when it runs the app.

## Test / lint

```bash
cargo test
cargo clippy -- -D warnings
cargo fmt --check
```

## Docker

```bash
docker build -t {{ cookiecutter.project_slug }} .
docker run --rm -p 8000:8000 {{ cookiecutter.project_slug }}
```

The image is multi-stage and runs as a non-root user.

## API

| Route | Answers |
|---|---|
| `GET /health` | `{"status": "ok", "version": "…"}` |
| `GET /api/v1/items` | every item |
| `POST /api/v1/items` | creates one from `{"name": "…"}`; `201`, `422` on a bad name, `400` on bad JSON |
| `GET /api/v1/items/{id}` | one item or `404` |

## Layout

```
src/
├── main.rs               main only: PORT, listener, graceful shutdown
├── lib.rs                the router and every route; VERSION
├── handlers/             HTTP: parse the request, call a service, write the response
│   ├── health.rs         GET /health
│   └── items.rs          the example resource: list, create, get
├── services/             business rules; never import axum; return errors handlers translate
└── models.rs             the structs that cross the HTTP boundary
tests/api.rs              the HTTP contract through the router
```

Request → route → handler → service → response. A handler holds no rules; a service holds no HTTP. Add `repositories/` when a database or an external API appears, and `middleware/` when a route needs auth or logging.
