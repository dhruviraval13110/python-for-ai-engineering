"""Binary logistic regression with gradient descent."""
from __future__ import annotations
import numpy as np

def sigmoid(z):
    z = np.clip(z, -500, 500)
    return 1 / (1 + np.exp(-z))

def fit(X, y, lr=0.1, epochs=1000):
    X = np.asarray(X, dtype=float); y = np.asarray(y, dtype=float)
    w = np.zeros(X.shape[1]); b = 0.0; history=[]
    for _ in range(epochs):
        p = sigmoid(X @ w + b)
        eps=1e-12
        loss = -np.mean(y*np.log(p+eps)+(1-y)*np.log(1-p+eps))
        history.append(float(loss))
        grad_w = X.T @ (p-y) / len(X)
        grad_b = float(np.mean(p-y))
        w -= lr*grad_w; b -= lr*grad_b
    return w,b,history

def predict_proba(X,w,b): return sigmoid(np.asarray(X) @ w + b)
def predict(X,w,b,threshold=0.5): return (predict_proba(X,w,b)>=threshold).astype(int)
