from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[2]

CONFIG_FILE = PROJECT_ROOT / "config" / "settings.yaml"


def load_config():
    """Load the application configuration from YAML."""
    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)

# from dataclasses import dataclass
# import os

# from dotenv import load_dotenv

# # Load variables from .env (if present)
# load_dotenv()


# @dataclass(frozen=True)
# class Settings:
#     APP_NAME: str = os.getenv("APP_NAME", "Enterprise AI Platform")
#     LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")


# settings = Settings()