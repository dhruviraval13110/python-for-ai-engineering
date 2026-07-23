"""
Tests for utility functions.
"""

from src.utils import current_time


def test_current_time_returns_string():
    """current_time() should return a string."""
    assert isinstance(current_time(), str)
