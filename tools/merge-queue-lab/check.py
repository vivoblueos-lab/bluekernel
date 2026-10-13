"""Small deterministic integration check for the merge queue experiment."""
from pathlib import Path

root = Path(__file__).resolve().parent
lower = int((root / "lower.txt").read_text().strip())
upper = int((root / "upper.txt").read_text().strip())
print(f"Integration constraint: {lower} <= {upper}", flush=True)
if lower > upper:
    raise SystemExit("Incompatible combined changes: lower exceeds upper")
