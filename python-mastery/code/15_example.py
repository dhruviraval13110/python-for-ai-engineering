"""Chapter 15: NumPy vectorization."""

import numpy as np

x = np.array([1, 2, 3], dtype=np.float64)
print("shape:", x.shape)
print("dtype:", x.dtype)
print("scaled:", x * 10)
print("mean:", x.mean())
