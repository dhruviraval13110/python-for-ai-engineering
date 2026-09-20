"""Small, testable sales analytics pipeline."""
from __future__ import annotations
import pandas as pd

REQUIRED = {"order_id", "date", "region", "category", "quantity", "revenue"}

def clean_sales(df: pd.DataFrame) -> pd.DataFrame:
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    out = df.copy()
    out["date"] = pd.to_datetime(out["date"], errors="coerce")
    out["quantity"] = pd.to_numeric(out["quantity"], errors="coerce")
    out["revenue"] = pd.to_numeric(out["revenue"], errors="coerce")
    out = out.dropna(subset=["date", "quantity", "revenue"])
    out = out[out["quantity"] > 0]
    out = out[out["revenue"] >= 0]
    return out.drop_duplicates(subset=["order_id"]).reset_index(drop=True)

def monthly_summary(df: pd.DataFrame) -> pd.DataFrame:
    clean = clean_sales(df)
    return (
        clean.assign(month=clean["date"].dt.to_period("M").astype(str))
        .groupby("month", as_index=False)
        .agg(orders=("order_id", "nunique"), units=("quantity", "sum"), revenue=("revenue", "sum"))
        .sort_values("month")
    )

def category_summary(df: pd.DataFrame) -> pd.DataFrame:
    clean = clean_sales(df)
    return (
        clean.groupby("category", as_index=False)
        .agg(orders=("order_id", "nunique"), revenue=("revenue", "sum"))
        .sort_values("revenue", ascending=False)
    )
