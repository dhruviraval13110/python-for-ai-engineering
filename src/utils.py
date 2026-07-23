"""
Utility functions.
"""

from datetime import datetime


def print_banner() -> None:
    """Print the project banner."""

    print("=" * 50)
    print("Python for AI Engineering")
    print("AI • Machine Learning • Software Engineering")
    print("=" * 50)


def current_time() -> str:
    """Return current timestamp."""

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
