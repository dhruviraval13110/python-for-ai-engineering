"""Chapter 19: measure before optimizing."""

import time

def slow_sum(values):
    total = 0
    for value in values:
        total += value
    return total

values = range(1_000_000)
start = time.perf_counter()
result = slow_sum(values)
elapsed = time.perf_counter() - start
print(result, f"{elapsed:.6f}s")
