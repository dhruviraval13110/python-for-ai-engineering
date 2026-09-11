# Calculus for ML

## Gradient intuition
A gradient points toward the direction of greatest local increase. Optimization commonly moves in the opposite direction.

For a scalar function $f(w)$, gradient descent uses: $w_{t+1}=w_t-\eta
abla f(w_t)$.

## Finite-difference check
```python
def numerical_gradient(f, x, eps=1e-6):
    return (f(x + eps) - f(x - eps)) / (2 * eps)
```

Use numerical gradients to sanity-check analytic derivatives in small experiments.
