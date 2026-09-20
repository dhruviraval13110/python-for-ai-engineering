"""Chapter 16: Pandas transformation."""

import pandas as pd

df = pd.DataFrame({"region": ["West", "West", "North"], "sales": [100, 150, 80]})
summary = df.groupby("region", as_index=False)["sales"].sum()
print(summary)
