"""
General utility functions for the Enterprise AI Platform.
"""

from pathlib import Path


def get_project_root() -> Path:
    """
    Return the repository root directory.
    """
    return Path(__file__).resolve().parents[2]