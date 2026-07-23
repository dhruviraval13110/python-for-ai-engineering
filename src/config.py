"""
Project configuration.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

DOCS_DIR = PROJECT_ROOT / "docs"

PROJECTS_DIR = PROJECT_ROOT / "projects"

LOG_DIR = PROJECT_ROOT / "logs"

LOG_DIR.mkdir(exist_ok=True)
