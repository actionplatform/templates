# {{ cookiecutter.project_name }}

{% if cookiecutter.description %}{{ cookiecutter.description }}

{% endif %}## Run

```bash
composer install
touch database/database.sqlite
php artisan migrate
php artisan serve --port=8000        # http://localhost:8000/health
```

`PORT` overrides the listen port in the Docker image (default `8000`) — the platform sets it when it runs the app. Stateless API: no `APP_KEY` is needed until you add encryption or sessions.

## Test / lint

```bash
composer test         # phpunit
composer lint         # pint --test
composer analyse      # larastan
composer format       # pint, writes
```

## Docker

```bash
docker build -t {{ cookiecutter.project_slug }} .
docker run --rm -p 8000:8000 {{ cookiecutter.project_slug }}
```

The image is multi-stage, runs as a non-root user and migrates the SQLite database on start.

## API

| Route | Answers |
|---|---|
| `GET /health` | `{"status": "ok", "version": "…"}` |
| `GET /api/v1/items` | every item |
| `POST /api/v1/items` | creates one from `{"name": "…"}`; `201`, `422` on a bad name |
| `GET /api/v1/items/{id}` | one item or `404` |

Errors are always JSON, with or without an `Accept` header.

## Layout

```
app/
├── Http/Controllers/     HTTP: call the model, write the response (HealthController, ItemController)
├── Http/Requests/        validation rules for a request body
├── Models/               Eloquent models
└── Providers/
bootstrap/app.php         routing: /health, /api/v1 from routes/api.php; JSON errors
config/                   app, cache, database, logging
database/                 migrations, factories, the SQLite file
routes/api.php            every API route
tests/Feature/            the HTTP contract
.code_quality/            pint.json, phpstan.neon (larastan)
```

Request → route → controller → request validation → model → response. Move rules into `app/Services/` when a controller grows past parsing and answering.
