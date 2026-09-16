# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Run

```bash
poetry install --with dev,code-quality
poetry run uvicorn app:app --port 8000      # http://localhost:8000/mcp  +  /health
poetry run python server.py                 # stdio, for local MCP clients
```

Register in a client (`.mcp.json`):

```json
{ "mcpServers": { "{{ cookiecutter.project_slug }}": { "type": "http", "url": "http://localhost:8000/mcp" } } }
```

## Test / lint

```bash
poetry run pytest
poetry run ruff check .
```

## Layout

```
app/__init__.py    # FastMCP instance, /health, create_app()  ← convention for every web/python/*
server.py          # stdio entry point
tools/hello.py     # one module per tool, plain functions
tests/             # tool via in-memory Client, /health via TestClient
```
