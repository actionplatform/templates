"""Reads the authenticated token's claims."""

from fastmcp.server.dependencies import get_access_token


def whoami() -> dict:
    """Return the subject and scopes of the caller's token."""
    token = get_access_token()
    if token is None:
        return {"authenticated": False}
    return {
        "authenticated": True,
        "subject": token.claims.get("sub"),
        "scopes": token.scopes,
    }
