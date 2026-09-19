from __future__ import annotations
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error
from .model import _model, MODEL_NAMES

def _select_model(train,feature_columns,target_column):
    test_size=max(10,int(len(train)*0.20));split=max(60,len(train)-test_size)
    inner_train=train.iloc[:split];inner_test=train.iloc[split:]
    scores={}
    for name in MODEL_NAMES:
        m=_model(name);m.fit(inner_train[feature_columns],inner_train[target_column])
        scores[name]=mean_absolute_error(inner_test[target_column],m.predict(inner_test[feature_columns]))
    scores["zero_baseline"]=mean_absolute_error(inner_test[target_column],np.zeros(len(inner_test)))
    return min(scores,key=scores.get)

def walk_forward_backtest(features,feature_columns,target_column,min_train_rows=80,max_folds=20,step=21,model_name="auto"):
    clean=features.dropna(subset=feature_columns+[target_column]).copy()
    if len(clean)<=min_train_rows:return pd.DataFrame(columns=["forecast_date","target_return","predicted_return","error","abs_error","model_name"])
    origins=list(range(min_train_rows,len(clean),max(1,step)))[-max_folds:];rows=[]
    for origin in origins:
        train=clean.iloc[:origin];test=clean.iloc[[origin]]
        selected=_select_model(train,feature_columns,target_column) if model_name=="auto" else model_name
        if selected=="zero_baseline":predicted=0.0
        else:
            model=_model(selected);model.fit(train[feature_columns],train[target_column]);predicted=float(model.predict(test[feature_columns])[0])
        actual=float(test[target_column].iloc[0]);error=actual-predicted
        rows.append({"forecast_date":clean.index[origin].date().isoformat(),"target_return":actual,"predicted_return":predicted,"error":error,"abs_error":abs(error),"model_name":selected})
    return pd.DataFrame(rows)

def summarize_backtest(results):
    if results.empty:return {"folds":0,"mean_abs_error":np.nan,"mean_error":np.nan,"direction_accuracy":np.nan,"price_return_mae":np.nan,"error_p80":np.nan,"error_median":np.nan}
    actual=results["target_return"];predicted=results["predicted_return"]
    return {"folds":int(len(results)),"mean_abs_error":float(results["abs_error"].mean()),"mean_error":float(results["error"].mean()),"direction_accuracy":float((np.sign(actual)==np.sign(predicted)).mean()),"price_return_mae":float(mean_absolute_error(actual,predicted)),"error_p80":float(results["abs_error"].quantile(0.80)),"error_median":float(results["error"].median())}
