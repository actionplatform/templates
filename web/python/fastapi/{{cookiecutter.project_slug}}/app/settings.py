"""Settings loaded from environment variables (and `.env` locally)."""

from __future__ import annotations

import logging
import secrets
from functools import lru_cache
from typing import Literal

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger(__name__)

_WEAK_SECRET_KEYS = {"", "secret", "changeme", "your-secret-key"}


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    scope: Literal["development", "production"] = "development"
    api_version: str = "0.1.0"
    api_v1_prefix: str = "/api/v1"
    cors_origins: list[str] = ["http://localhost:3000"]
    secret_key: str = ""

    @field_validator("cors_origins", mode="before")
    @classmethod
    def _split_origins(cls, value: str | list[str]) -> list[str]:
        if isinstance(value, str):
            return [
                origin.strip() for origin in value.split(",") if origin.strip()
            ]
        return value

    @field_validator("secret_key")
    @classmethod
    def _validate_secret_key(cls, value: str, info) -> str:
        if info.data.get("scope") == "production":
            if len(value) < 32 or value in _WEAK_SECRET_KEYS:
                raise ValueError(
                    "SECRET_KEY must be at least 32 chars in production"
                )
            return value
        if not value:
            logger.warning("No SECRET_KEY set — using an ephemeral key")
            return secrets.token_hex(32)
        return value

    @property
    def is_development(self) -> bool:
        return self.scope == "development"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
