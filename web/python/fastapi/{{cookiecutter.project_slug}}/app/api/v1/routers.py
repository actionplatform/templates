"""Aggregate every v1 router here."""

from fastapi import APIRouter

from app.api.v1.health import health_router

v1 = APIRouter()
v1.include_router(health_router, prefix="/health", tags=["Health"])
