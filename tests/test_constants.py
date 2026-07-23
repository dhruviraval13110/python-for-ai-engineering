"""
Tests for project constants.
"""

from src.constants import APP_NAME, VERSION


def test_app_name():
    """APP_NAME should be a non-empty string."""
    assert isinstance(APP_NAME, str)
    assert APP_NAME != ""


def test_version():
    """VERSION should be defined."""
    assert isinstance(VERSION, str)
