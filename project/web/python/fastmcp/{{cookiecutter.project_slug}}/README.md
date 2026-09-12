# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Run

```bash
poetry install --with dev,code-quality
poetry run python server.py                 # stdio
poetry run fastmcp run server.py --transport http --port 8000   # http
```

Register in a client (`.mcp.json`):

```json
{ "mcpServers": { "{{ cookiecutter.project_slug }}": { "command": "poetry", "args": ["run", "python", "server.py"] } } }
```

## Test / lint

```bash
poetry run pytest
poetry run ruff check .
```

## Layout

```
server.py          # FastMCP instance, registers tools
tools/hello.py     # one module per tool, plain functions
tests/             # calls tools through the in-memory Client
```
