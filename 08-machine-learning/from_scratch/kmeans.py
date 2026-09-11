"""Minimal K-Means implementation for learning purposes."""
from __future__ import annotations
import numpy as np

def fit(X, k=3, max_iter=100, seed=42):
    X=np.asarray(X,dtype=float); rng=np.random.default_rng(seed)
    centers=X[rng.choice(len(X), size=k, replace=False)].copy()
    for _ in range(max_iter):
        distances=((X[:,None,:]-centers[None,:,:])**2).sum(axis=2)
        labels=distances.argmin(axis=1)
        new=np.array([X[labels==i].mean(axis=0) if np.any(labels==i) else centers[i] for i in range(k)])
        if np.allclose(new,centers): break
        centers=new
    return centers, labels
