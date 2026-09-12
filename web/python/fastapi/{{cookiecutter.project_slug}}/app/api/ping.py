"""Liveness probe."""

from fastapi import APIRouter

ping_router = APIRouter(tags=["Ping"])


@ping_router.get("", include_in_schema=False)
def get_status() -> dict[str, str]:
    return {"status": "it's alive"}
