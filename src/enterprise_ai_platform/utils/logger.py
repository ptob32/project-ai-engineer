"""
Logging utilities for the Enterprise AI Platform.
"""

from pathlib import Path
import logging

from enterprise_ai_platform.utils.paths import get_project_root

def configure_logging() -> None:
    """Configure application-wide logging."""

    root_logger = logging.getLogger()

    if root_logger.handlers:
        return

    log_directory = get_project_root() / "logs"
    log_directory.mkdir(exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    log_file = log_directory / "application.log"

    file_handler = logging.RotatingFileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

def get_logger(name: str) -> logging.Logger:
    """Return a logger for the given module."""
    return logging.getLogger(name)
    
