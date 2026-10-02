"""Environment-only runtime configuration."""
import os


def _required(name: str) -> str:
    value = os.getenv(name)
    if value is None or not value.strip():
        raise RuntimeError(f"Required environment variable {name} is not set")
    return value.strip()


def get_log_level() -> str:
    return os.getenv("RETAIL_AGENT_LOG_LEVEL", "INFO").upper()


def get_timeout_seconds() -> int:
    raw = os.getenv("RETAIL_AGENT_TIMEOUT_SECONDS", "30")
    try:
        value = int(raw)
    except ValueError as exc:
        raise RuntimeError("RETAIL_AGENT_TIMEOUT_SECONDS must be an integer") from exc
    if value <= 0:
        raise RuntimeError("RETAIL_AGENT_TIMEOUT_SECONDS must be positive")
    return value


def get_runtime_profile() -> str:
    return os.getenv("RETAIL_AGENT_RUNTIME_PROFILE", "local").strip() or "local"
