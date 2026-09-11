# Linear Algebra for ML

## Mental model
Vectors represent features or directions; matrices represent transformations or collections of vectors.

### Vector
A vector is an ordered collection of numbers: $x = [x_1, ..., x_n]^T$.

### Dot product
$w^Tx = \sum_i w_i x_i$. In ML this is the core computation behind a linear model.

### Matrix multiplication
For compatible matrices, $(AB)_{ij}=\sum_k A_{ik}B_{kj}$. Think of it as composing transformations.

### Runnable experiment
```python
import numpy as np

x = np.array([2.0, 3.0])
w = np.array([0.5, -1.0])
b = 4.0
y = w @ x + b
print(y)
```

### From scratch: linear prediction
```python
def predict(X, w, b):
    return X @ w + b
```

### ML connection
Linear regression, logistic regression, PCA, neural-network layers and attention all rely heavily on vector/matrix operations.

### Exercises
1. Compute a dot product by hand.
2. Implement matrix multiplication with nested loops.
3. Compare loop and NumPy implementations.
4. Explain why shapes matter.
