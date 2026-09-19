import numpy as np
import pandas as pd
from src.backtest import summarize_backtest,walk_forward_backtest
def _features(n=260):
    idx=pd.date_range("2020-01-01",periods=n,freq="B");x=np.arange(n);return pd.DataFrame({"feature":np.sin(x/10),"target":0.05*np.sin(x/10)+0.01*np.cos(x/7)},index=idx)
def test_walk_forward_is_chronological_and_selects_models():
    r=walk_forward_backtest(_features(),["feature"],"target",80,5,20,"auto")
    assert len(r)==5;assert r["forecast_date"].is_monotonic_increasing;assert r["abs_error"].ge(0).all();assert r["model_name"].isin(["hist","extra_trees","zero_baseline"]).all()
def test_backtest_summary_reports_direction_accuracy():
    r=pd.DataFrame({"target_return":[.1,-.1,.2],"predicted_return":[.05,-.03,-.02],"error":[.05,.07,-.22],"abs_error":[.05,.07,.22]})
    s=summarize_backtest(r);assert s["folds"]==3;assert s["direction_accuracy"]==2/3
