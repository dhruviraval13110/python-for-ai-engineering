# Sales Analytics Pipeline

A testable Pandas pipeline for cleaning transactional data and producing monthly/category summaries.

**Status:** Implemented learning project using small in-memory examples for reproducibility.

## Run

```bash
cd projects/sales-analytics
pip install pandas pytest
PYTHONPATH=src pytest -q
```

## Design

`clean_sales()` validates the data contract, parses dates, coerces numeric fields, removes invalid transactions, and deduplicates order IDs. Reporting functions operate on the cleaned table rather than mixing cleaning logic with analysis.

## Why this matters

This project demonstrates a core AI/data-engineering habit: separate **data quality**, **transformation**, and **analysis** so each layer can be tested independently.

## Next steps

- add a real licensed dataset
- add schema validation
- add visualization notebook
- add partitioned input/output
- benchmark larger datasets
