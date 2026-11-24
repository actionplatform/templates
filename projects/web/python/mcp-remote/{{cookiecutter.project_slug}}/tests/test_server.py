import httpx
import pytest
from fastmcp import Client
from fastmcp.client.auth import BearerAuth
from fastmcp.client.transports import StreamableHttpTransport
from fastmcp.server.auth import JWTVerifier, RemoteAuthProvider
from fastmcp.server.auth.providers.jwt import RSAKeyPair

from app import __version__, auth, build_mcp, create_app
from tools.hello import hello

ISSUER = "https://auth.example.com/"
AUDIENCE = "https://mcp.example.com/mcp"
BASE_URL = "http://testserver"
MCP_URL = f"{BASE_URL}/mcp"


@pytest.fixture(scope="module")
def keys():
    return RSAKeyPair.generate()


@pytest.fixture
def app(keys):
    verifier = JWTVerifier(
        public_key=keys.public_key,
        issuer=ISSUER,
        audience=AUDIENCE,
        base_url=BASE_URL,
    )
    provider = RemoteAuthProvider(
        token_verifier=verifier,
        authorization_servers=[ISSUER],  # type: ignore[list-item]
        base_url=BASE_URL,
    )
    return create_app(stateless=True, auth=provider)


def token(keys, **overrides):
    claims = {
        "subject": "ana",
        "issuer": ISSUER,
        "audience": AUDIENCE,
        **overrides,
    }
    return keys.create_token(**claims)


def http(app):
    return httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url=BASE_URL
    )


def test_hello_function():
    assert hello() == "hello, world"
    assert hello("ana") == "hello, ana"


async def test_health_is_public(app):
    async with app.router.lifespan_context(app), http(app) as client:
        response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": __version__}


async def test_mcp_without_token_is_401(app):
    async with app.router.lifespan_context(app), http(app) as client:
        response = await client.post("/mcp", json={})
    assert response.status_code == 401
    assert "bearer" in response.headers["www-authenticate"].lower()


@pytest.mark.parametrize(
    "overrides",
    [{"audience": "https://other.example.com"}, {"expires_in_seconds": -60}],
)
async def test_mcp_with_invalid_token_is_401(app, keys, overrides):
    bad = token(keys, **overrides)
    async with app.router.lifespan_context(app), http(app) as client:
        response = await client.post(
            "/mcp", json={}, headers={"Authorization": f"Bearer {bad}"}
        )
    assert response.status_code == 401


async def test_tools_with_valid_token(app, keys):
    def factory(**kwargs):
        kwargs.pop("transport", None)
        return httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), **kwargs
        )

    transport = StreamableHttpTransport(
        MCP_URL,
        auth=BearerAuth(token(keys, scopes=["read"])),
        httpx_client_factory=factory,  # type: ignore[arg-type]
    )
    async with app.router.lifespan_context(app), Client(transport) as client:
        names = sorted(t.name for t in await client.list_tools())
        greeting = await client.call_tool("hello", {"name": "ana"})
        who = await client.call_tool("whoami", {})
    assert names == ["hello", "whoami"]
    assert greeting.data == "hello, ana"
    assert who.data == {
        "authenticated": True,
        "subject": "ana",
        "scopes": ["read"],
    }


async def test_protected_resource_metadata(app):
    async with app.router.lifespan_context(app), http(app) as client:
        response = await client.get(
            "/.well-known/oauth-protected-resource/mcp"
        )
    assert response.status_code == 200
    body = response.json()
    assert body["authorization_servers"] == [ISSUER]
    assert body["resource"] == MCP_URL


async def test_stdio_server_has_no_auth():
    async with Client(build_mcp()) as client:
        result = await client.call_tool("whoami", {})
    assert result.data == {"authenticated": False}


def test_env_auth_requires_all_variables(monkeypatch):
    monkeypatch.delenv("MCP_AUTH_DISABLED", raising=False)
    for name in auth.REQUIRED:
        monkeypatch.delenv(name, raising=False)
    with pytest.raises(RuntimeError, match="MCP_JWKS_URI"):
        auth.auth_from_env()


def test_env_auth_builds_provider(monkeypatch):
    monkeypatch.delenv("MCP_AUTH_DISABLED", raising=False)
    env = {
        "MCP_JWKS_URI": f"{ISSUER}.well-known/jwks.json",
        "MCP_ISSUER": ISSUER,
        "MCP_AUDIENCE": AUDIENCE,
        "MCP_BASE_URL": BASE_URL,
        "MCP_AUTHORIZATION_SERVER": ISSUER,
    }
    for name, value in env.items():
        monkeypatch.setenv(name, value)
    assert isinstance(auth.auth_from_env(), RemoteAuthProvider)


def test_auth_is_disabled_only_explicitly(monkeypatch):
    monkeypatch.setenv("MCP_AUTH_DISABLED", "true")
    assert auth.auth_from_env() is None
