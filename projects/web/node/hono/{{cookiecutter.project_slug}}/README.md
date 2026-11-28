# {{ cookiecutter.project_name }}

{% if cookiecutter.description %}{{ cookiecutter.description }}

{% endif %}## Install

```bash
nvm use
npm ci
```

## Run

```bash
npm run dev            # http://localhost:8000/health (reloads on change)
npm run build && npm start
```

`PORT` and `HOST` override `8000` / `0.0.0.0`.

## Test

```bash
npm test               # Vitest, app.request(), no network
npm run lint
npm run format
npm run typecheck
npm run build
```

## Docker

```bash
docker build -t {{ cookiecutter.project_slug }} .
docker run --rm -p 8000:8000 {{ cookiecutter.project_slug }}
```

The image runs `node dist/server.js` as a non-root user with production dependencies only and listens on `$PORT` (default `8000`).

## Endpoints

```
GET  /health               {"status": "ok", "version": "0.0.0"}
GET  /api/v1/items         [{"id": 1, "name": "pen"}]
POST /api/v1/items         {"name": "pen"} -> 201; 422 when the name is blank or over 40 characters
GET  /api/v1/items/:id     404 when unknown
```

Errors share one shape: `{"error": "message"}`.

## Layout

```
src/
├── app.ts            createApp(): routes and error handling; VERSION lives in version.ts
├── server.ts         starts the server, nothing else
├── errors.ts         domain errors
├── api/
│   ├── health.ts     GET /health
│   └── v1/items.ts   HTTP only
└── services/
    └── items.ts      rules and in-memory store — replace the store
tests/
├── health.test.ts
├── items.test.ts           app.request()
└── items.service.test.ts
```
