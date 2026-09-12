"""Aggregate every v1 router here."""

from fastapi import APIRouter

from app.api.v1.hello import hello_router

v1 = APIRouter()
v1.include_router(hello_router, prefix="/hello", tags=["Hello"])
