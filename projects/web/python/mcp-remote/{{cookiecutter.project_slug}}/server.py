"""Local entry point: `python server.py` (stdio, no auth) or `uvicorn app:app` (http, bearer auth)."""

from app import build_mcp

if __name__ == "__main__":
    build_mcp().run()
