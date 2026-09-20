"""Chapter 13: typing."""

from collections.abc import Sequence

def average(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("values cannot be empty")
    return sum(values) / len(values)

print(average([1.0, 2.0, 3.0]))
