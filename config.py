"""Environment-driven settings. Fails closed when required config is missing."""
from __future__ import annotations

import os
from dataclasses import dataclass


class ConfigError(RuntimeError):
    pass


def require_database_url() -> str:
    url = os.environ.get("DATABASE_URL", "").strip()
    if not url:
        raise ConfigError("DATABASE_URL is not set; refusing to start (no silent default).")
    return url


def default_country_code() -> str:
    return os.environ.get("DEFAULT_COUNTRY_CODE", "+91").strip() or "+91"


def dev_auth_token() -> str | None:
    tok = os.environ.get("DEV_AUTH_TOKEN", "").strip()
    return tok or None


def auto_create_tables() -> bool:
    return os.environ.get("AUTO_CREATE_TABLES", "false").lower() == "true"


@dataclass(frozen=True)
class CallingSettings:
    mode: str  # "mock" is the only supported mode
    live_calls_enabled: bool


def calling_settings() -> CallingSettings:
    return CallingSettings(
        mode=os.environ.get("CALLING_MODE", "mock").strip().lower(),
        live_calls_enabled=os.environ.get("LIVE_CALLS_ENABLED", "false").strip().lower() == "true",
    )
