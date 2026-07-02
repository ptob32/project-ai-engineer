"""
Logging utilities for the Enterprise AI Platform.
"""

import logging

from enterprise_ai_platform.config import settings


def get_logger(name: str) -> logging.Logger:
    """
    Create and configure a logger.

    Parameters
    ----------
    name:
        Usually pass __name__ from the calling module.
    """
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(settings.LOG_LEVEL)

    handler = logging.StreamHandler()
    handler.setLevel(settings.LOG_LEVEL)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.propagate = False

    return logger