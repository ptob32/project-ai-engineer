from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_FILE = PROJECT_ROOT / "config" / "settings.yaml"
ENV_FILE = PROJECT_ROOT / ".env"


def load_config() -> dict[str, Any]:
    """Load application configuration from YAML and environment variables."""

    load_dotenv(ENV_FILE)

    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file) or {}

    config.setdefault("environment", {})
    config["environment"]["name"] = os.getenv("APP_ENV", "development")
    config["environment"]["database_url"] = os.getenv(
        "DATABASE_URL",
        "sqlite:///data/app.db",
    )

    config.setdefault("logging", {})
    config["logging"]["level"] = os.getenv(
        "LOG_LEVEL",
        config["logging"].get("level", "INFO"),
    )

    return config