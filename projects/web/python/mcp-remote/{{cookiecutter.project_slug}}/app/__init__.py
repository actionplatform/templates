__version__ = "0.0.0"

import os

from fastmcp import FastMCP
from fastmcp.server.auth import AuthProvider
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.auth import auth_from_env
from tools.hello import hello


def build_mcp(auth: AuthProvider | None = None) -> FastMCP:
    mcp = FastMCP("{{ cookiecutter.project_name }}", version=__version__, auth=auth)
    mcp.tool(hello)

    @mcp.custom_route("/health", methods=["GET"])
    async def health(_: Request) -> JSONResponse:
        return JSONResponse({"status": "ok", "version": __version__})

    return mcp


def create_app(
    stateless: bool | None = None, auth: AuthProvider | None = None
):
    if stateless is None:
        stateless = bool(os.environ.get("AWS_LAMBDA_FUNCTION_NAME"))
    mcp = build_mcp(auth or auth_from_env())
    return mcp.http_app(
        path="/mcp", stateless_http=stateless, json_response=stateless
    )


def __getattr__(name: str):
    if name == "app":
        return create_app()
    raise AttributeError(name)
