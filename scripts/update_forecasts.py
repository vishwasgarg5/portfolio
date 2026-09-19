from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from src.pipeline import run
from src.report import build_report

if __name__=="__main__":
    result=run(update_data=True)
    build_report()
    print(f"Forecasts completed: {(result['status']=='ok').sum()}/{len(result)} stocks")
    print("Report written to predictions/portfolio_report.csv and predictions/portfolio_report.md")
