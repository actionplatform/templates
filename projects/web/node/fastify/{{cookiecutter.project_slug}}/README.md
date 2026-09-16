# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Install

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

## Test / lint

```bash
npm test
npm run lint
npm run format
npm run build
```

## Endpoints

```
GET /health                       {"status": "ok", "version": "0.0.0"}
GET /api/v1/hello?name=Fernando {"message": "hello, Fernando"}
```

## Layout

```
src/
├── app.ts          createApp(): builds and returns the Fastify instance; VERSION
├── server.ts       starts the server, nothing else
└── api/
    ├── health.ts     GET /health
    └── v1/
        ├── router.ts   mounts every v1 route
        └── hello.ts    GET /hello — replace with real resources
tests/
├── health.test.ts
└── hello.test.ts   app.inject(), no network
```
