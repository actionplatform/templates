"""{{ cookiecutter.project_name }} — MCP server entry point."""

from fastmcp import FastMCP

from tools.hello import hello

__version__ = "0.1.0"

mcp = FastMCP("{{ cookiecutter.project_name }}", version=__version__)

mcp.tool(hello)

if __name__ == "__main__":
    mcp.run()
