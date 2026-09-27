from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import pandas as pd
from src.data import load_history
from src.strategy_backtest import run_strategy_backtest, DETERIORATION_DAYS
ROOT=Path(__file__).resolve().parents[1]
stocks=pd.read_csv(ROOT/"config"/"stocks.csv")
rows=[]
for days in (3,5,7):
    for r in stocks.to_dict("records"):
        try:
            prices=load_history(str(r["symbol"]))
            out=run_strategy_backtest(prices,str(r["symbol"]),str(r["name"]),float(r["shares"]),float(r["purchase_price"]),deterioration_days=days)
            for x in out:
                x=dict(x); x["grace_days"]=days
                rows.append(x)
        except Exception as exc:
            rows.append({"symbol":r["symbol"],"name":r["name"],"grace_days":days,"decision":f"error: {exc}"})
df=pd.DataFrame(rows)
df.to_csv(ROOT/"predictions"/"v61_grace_experiment.csv",index=False)
plans=df[df.decision.eq("plan")].copy()
lines=["# V6.1 Grace-Period Experiment","",f"- Baseline V6 deterioration days: {DETERIORATION_DAYS}"]
for d,g in plans.groupby("grace_days"):
    exits=g.exit_type.value_counts()
    lines += ["",f"## {d}-day grace period",f"- Plans: {len(g)}",f"- Target exits: {int((g.exit_type=='target').sum())} ({(g.exit_type=='target').mean()*100:.1f}%)",f"- Deterioration exits: {int((g.exit_type=='deterioration').sum())} ({(g.exit_type=='deterioration').mean()*100:.1f}%)",f"- Stop-loss exits: {int((g.exit_type=='stop_loss').sum())} ({(g.exit_type=='stop_loss').mean()*100:.1f}%)",f"- Positive partial outcomes: {(g.partial_profit_percent>0).mean()*100:.1f}%",f"- Mean partial outcome: {g.partial_profit_percent.mean()*100:.2f}%",f"- Median partial outcome: {g.partial_profit_percent.median()*100:.2f}%",f"- Mean capital deployed: ₹{g.capital_deployed.mean():,.0f}",f"- Mean exit days: {((pd.to_datetime(g.exit_date)-pd.to_datetime(g.plan_date)).dt.days).mean():.1f}"]
lines += ["","## Decision rule","- V6 remains the control. V6.1 is considered for further testing only if a grace period improves target/positive outcomes without materially increasing downside or capital deployment."]
(ROOT/"predictions"/"v61_grace_experiment.md").write_text("\n".join(lines)+"\n")
print("\n".join(lines))
