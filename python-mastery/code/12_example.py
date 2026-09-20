"""Chapter 12: generators and decorators."""

from collections.abc import Iterator
from functools import wraps

def batches(items: list[int], size: int) -> Iterator[list[int]]:
    for start in range(0, len(items), size):
        yield items[start:start + size]

def announce(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("running", fn.__name__)
        return fn(*args, **kwargs)
    return wrapper

@announce
def total(values):
    return sum(values)

print(list(batches(list(range(7)), 3)))
print(total([1, 2, 3]))
