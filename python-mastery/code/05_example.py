"""Chapter 05: functions."""

from typing import Iterable

def mean(values: Iterable[float], *, default: float = 0.0) -> float:
    items = list(values)
    return sum(items) / len(items) if items else default

print(mean([10, 20, 30]))
