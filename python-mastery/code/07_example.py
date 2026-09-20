"""Chapter 07: text normalization."""

import re

def normalize(text: str) -> list[str]:
    cleaned = re.sub(r"[^a-z0-9\s]", " ", text.lower())
    return [token for token in cleaned.split() if token]

print(normalize("Python, AI & ML!"))
