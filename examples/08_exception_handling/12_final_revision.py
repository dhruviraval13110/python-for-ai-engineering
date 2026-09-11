"""Final executable revision for Python exception handling."""

from pathlib import Path


def safe_divide(left: float, right: float) -> float | None:
    """Return a quotient while handling expected invalid input."""
    try:
        return left / right
    except ZeroDivisionError:
        return None


def read_text(path: str) -> str | None:
    """Read a UTF-8 file and handle a missing file explicitly."""
    try:
        return Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return None


def main() -> None:
    print("Exception handling revision")
    print("divide(10, 2):", safe_divide(10, 2))
    print("divide(10, 0):", safe_divide(10, 0))
    print("missing file:", read_text("does-not-exist.txt"))
    print("Rules: catch specific errors; keep try blocks small; preserve useful context.")


if __name__ == "__main__":
    main()
