"""Bearer auth built from the environment."""

import os

from fastmcp.server.auth import AuthProvider, JWTVerifier, RemoteAuthProvider

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
    """JWT verification against the JWKS plus RFC 9728 metadata; `None` only when MCP_AUTH_DISABLED is set."""
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
        authorization_servers=[os.environ["MCP_AUTHORIZATION_SERVER"]],  # type: ignore[list-item]
        base_url=base_url,
    )
