import os

from fastmcp.server.auth import AuthProvider, JWTVerifier, RemoteAuthProvider
from pydantic import AnyHttpUrl

REQUIRED = (
    "MCP_JWKS_URI",
    "MCP_ISSUER",
    "MCP_AUDIENCE",
    "MCP_BASE_URL",
    "MCP_AUTHORIZATION_SERVER",
)


def auth_disabled() -> bool:
    return os.environ.get("MCP_AUTH_DISABLED", "").lower() in (
        "1",
        "true",
        "yes",
    )


def auth_from_env() -> AuthProvider | None:
    if auth_disabled():
        return None
    missing = [name for name in REQUIRED if not os.environ.get(name)]
    if missing:
        raise RuntimeError(
            f"missing env: {', '.join(missing)} (set MCP_AUTH_DISABLED=true to run without auth)"
        )
    base_url = os.environ["MCP_BASE_URL"]
    verifier = JWTVerifier(
        jwks_uri=os.environ["MCP_JWKS_URI"],
        issuer=os.environ["MCP_ISSUER"],
        audience=os.environ["MCP_AUDIENCE"],
        base_url=base_url,
    )
    return RemoteAuthProvider(
        token_verifier=verifier,
        authorization_servers=[
            AnyHttpUrl(os.environ["MCP_AUTHORIZATION_SERVER"])
        ],
        base_url=base_url,
    )
