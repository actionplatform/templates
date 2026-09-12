"""Local entry point: `python server.py` (stdio) or `uvicorn app:app` (http)."""

from app import mcp

if __name__ == "__main__":
    mcp.run()
