"""Linear regression trained with gradient descent."""
from __future__ import annotations
import numpy as np

def fit(X: np.ndarray, y: np.ndarray, lr: float = 0.01, epochs: int = 1000):
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float).reshape(-1)
    w = np.zeros(X.shape[1])
    b = 0.0
    history = []
    for _ in range(epochs):
        pred = X @ w + b
        error = pred - y
        loss = float(np.mean(error ** 2))
        history.append(loss)
        w -= lr * (2 / len(X)) * (X.T @ error)
        b -= lr * 2 * float(np.mean(error))
    return w, b, history

if __name__ == "__main__":
    X = np.array([[1.], [2.], [3.], [4.]])
    y = np.array([3., 5., 7., 9.])
    w, b, history = fit(X, y)
    print(f"w={w}, b={b}, final_mse={history[-1]:.6f}")
