"""Dummy endpoint. Replace with real resources."""

from fastapi import APIRouter

hello_router = APIRouter()


@hello_router.get("")
def get_hello(name: str = "world") -> dict[str, str]:
    return {"message": f"hello, {name}"}
