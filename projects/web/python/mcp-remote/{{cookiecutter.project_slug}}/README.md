# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

MCP over streamable HTTP at `/mcp`. Every request needs `Authorization: Bearer <jwt>`; the JWT is verified against the authorization server's JWKS (signature, issuer, audience, expiry). `/health` is public, and `/.well-known/oauth-protected-resource/mcp` publishes the OAuth protected resource metadata (RFC 9728) pointing clients to the authorization server.

## Configuration

Read from the environment where used (see `.env.example`):

| Variable | Meaning |
|----------|---------|
| `MCP_JWKS_URI` | JWKS the token signature is verified against |
| `MCP_ISSUER` | expected `iss` |
| `MCP_AUDIENCE` | expected `aud` |
| `MCP_BASE_URL` | public base URL of this server, used as the resource URL |
| `MCP_AUTHORIZATION_SERVER` | authorization server advertised in the resource metadata |
| `MCP_AUTH_DISABLED` | `true` runs without auth, for local development only |

Without `MCP_AUTH_DISABLED=true`, the app refuses to start unless the five `MCP_*` auth variables are set. Auth is never silently off.

## Run

```bash
poetry install --with dev,code-quality
poetry run uvicorn app:app --port 8000      # http://localhost:8000/mcp  +  /health
poetry run python server.py                 # stdio, no auth, for local MCP clients
```

Local run without an authorization server: `MCP_AUTH_DISABLED=true poetry run uvicorn app:app`.

On Lambda (`AWS_LAMBDA_FUNCTION_NAME` set) the transport is stateless.

## Test / lint

```bash
poetry run pytest
poetry run ruff check .
poetry run ruff format --check .
poetry run mypy --config-file .code_quality/mypy.ini .
```

## Layout

```
app/__init__.py    # build_mcp(), /health, create_app()  <- convention for every web/python/*
app/auth.py        # JWT verification + protected resource metadata, built from MCP_* env vars
server.py          # stdio entry point (no auth)
tools/hello.py     # one module per tool, plain functions
tools/whoami.py    # reads the authenticated token's claims
tests/             # signed tokens from a generated RSA key pair; no network
```
