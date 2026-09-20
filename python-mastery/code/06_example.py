"""Chapter 06: choosing data structures."""

records = [{"id": 1, "score": 0.91}, {"id": 2, "score": 0.73}]
best = max(records, key=lambda row: row["score"])
ids = {row["id"] for row in records}
print(best)
print(ids)
