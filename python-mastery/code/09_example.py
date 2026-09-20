"""Chapter 09: JSON and paths."""

import json
from pathlib import Path

data = {"project": "python-for-ai-engineering", "version": 1}
out = Path("example.json")
out.write_text(json.dumps(data, indent=2), encoding="utf-8")
print(json.loads(out.read_text(encoding="utf-8")))
out.unlink()
