"""End-to-end, leakage-safe customer churn training pipeline."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import json
import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

TARGET = "churned"
NUMERIC = ["tenure_months", "monthly_charges", "support_tickets", "usage_hours"]
CATEGORICAL = ["contract", "payment_method"]

@dataclass(frozen=True)
class TrainResult:
    metrics: dict[str, float]
    artifact: Path

def make_dataset(n: int = 600, seed: int = 42) -> pd.DataFrame:
    """Generate a deterministic synthetic dataset for reproducible learning."""
    rng = np.random.default_rng(seed)
    contracts = rng.choice(["monthly", "annual", "two_year"], n, p=[.55, .3, .15])
    payments = rng.choice(["card", "upi", "bank_transfer"], n)
    tenure = rng.integers(1, 61, n)
    charges = rng.normal(55, 18, n).clip(15, 130)
    tickets = rng.poisson(1.8, n)
    usage = rng.normal(28, 9, n).clip(2, 60)
    score = (
        1.2 * (contracts == "monthly")
        + 0.55 * (charges > 75)
        + 0.35 * (tickets >= 4)
        - 0.025 * tenure
        - 0.02 * usage
        + rng.normal(0, .35, n)
    )
    churn = (score > np.quantile(score, .68)).astype(int)
    return pd.DataFrame({
        "tenure_months": tenure, "monthly_charges": charges.round(2),
        "support_tickets": tickets, "usage_hours": usage.round(2),
        "contract": contracts, "payment_method": payments, TARGET: churn
    })

def build_pipeline() -> Pipeline:
    """Build preprocessing + classifier as one deployable artifact."""
    numeric = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])
    categorical = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ])
    preprocess = ColumnTransformer([
        ("numeric", numeric, NUMERIC),
        ("categorical", categorical, CATEGORICAL),
    ])
    return Pipeline([
        ("preprocess", preprocess),
        ("model", LogisticRegression(max_iter=1000, class_weight="balanced")),
    ])

def train(df: pd.DataFrame, artifact: Path) -> TrainResult:
    """Train, evaluate and persist the complete pipeline."""
    X, y = df.drop(columns=TARGET), df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=.2, random_state=42, stratify=y
    )
    model = build_pipeline()
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    proba = model.predict_proba(X_test)[:, 1]
    metrics = {
        "accuracy": accuracy_score(y_test, pred),
        "precision": precision_score(y_test, pred, zero_division=0),
        "recall": recall_score(y_test, pred, zero_division=0),
        "f1": f1_score(y_test, pred, zero_division=0),
        "roc_auc": roc_auc_score(y_test, proba),
    }
    artifact.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, artifact)
    return TrainResult(metrics=metrics, artifact=artifact)

if __name__ == "__main__":
    out = Path("artifacts/churn_pipeline.joblib")
    result = train(make_dataset(), out)
    print(json.dumps(result.metrics, indent=2))
