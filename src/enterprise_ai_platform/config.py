"""
Central configuration for the Enterprise AI Platform.

All application configuration should be accessed through the
Settings object rather than reading environment variables
directly throughout the codebase.
"""

from dataclasses import dataclass
import os

from dotenv import load_dotenv

# Load variables from .env (if present)
load_dotenv()


@dataclass(frozen=True)
class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "Enterprise AI Platform")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()