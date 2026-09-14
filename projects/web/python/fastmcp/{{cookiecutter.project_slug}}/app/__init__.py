"""{{ cookiecutter.project_name }} — MCP server as an ASGI app.

`create_app()` is the convention every `web/python/*` template follows: the
Lambda handler, uvicorn and tests all build the app through it.
"""

__version__ = "0.0.0"

import os

from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse

from tools.hello import hello

mcp = FastMCP("{{ cookiecutter.project_name }}", version=__version__)
mcp.tool(hello)


@mcp.custom_route("/ping", methods=["GET"])
async def ping(_: Request) -> JSONResponse:
    return JSONResponse({"status": "ok", "version": __version__})


def create_app(stateless: bool | None = None):
    """MCP over streamable HTTP at /mcp, ping at /ping.

    Stateless is forced on Lambda: nothing survives between invocations, so a
    session-bound transport would break on the second request.
    """
    if stateless is None:
        stateless = bool(os.environ.get("AWS_LAMBDA_FUNCTION_NAME"))
    return mcp.http_app(
        path="/mcp", stateless_http=stateless, json_response=stateless
    )


app = create_app()
