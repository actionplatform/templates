from fastmcp import Client

from server import mcp
from tools.hello import hello


def test_hello_function():
    assert hello() == "hello, world"
    assert hello("ana") == "hello, ana"


async def test_hello_tool_via_client():
    async with Client(mcp) as client:
        tools = await client.list_tools()
        assert [t.name for t in tools] == ["hello"]
        result = await client.call_tool("hello", {"name": "ana"})
        assert result.data == "hello, ana"
