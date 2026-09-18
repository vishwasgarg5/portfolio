from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.pipeline import run


if __name__ == "__main__":
    result = run(update_data=True)
    ok = (result["status"] == "ok").sum()
    print(f"Completed forecasts: {ok}/{len(result)} stocks")
    print(result[["symbol", "name", "current_price", "status"]].to_string(index=False))
