import pandas as pd
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from analytics import clean_sales, monthly_summary

def sample():
    return pd.DataFrame({
        "order_id": [1, 2, 2, 3],
        "date": ["2026-01-01", "2026-01-02", "bad", "2026-02-01"],
        "region": ["W", "N", "N", "S"],
        "category": ["A", "B", "B", "A"],
        "quantity": [2, 1, 1, -2],
        "revenue": [100, 50, 50, 20],
    })

def test_clean_sales_removes_invalid_rows_and_duplicates():
    out = clean_sales(sample())
    assert list(out["order_id"]) == [1, 2]

def test_monthly_summary():
    out = monthly_summary(sample())
    assert out.iloc[0]["orders"] == 2
    assert out.iloc[0]["revenue"] == 150
