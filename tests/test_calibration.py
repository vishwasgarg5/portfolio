import pandas as pd
from src.calibration import calibrate_return

def test_calibration_uses_historical_error_only():
    bt=pd.DataFrame({"error":[0.10,0.06,-0.02,0.08,0.04]})
    value,adjustment,n=calibrate_return(0.20,bt)
    assert n==5
    assert adjustment==0.03
    assert value==0.23

def test_calibration_does_not_adjust_with_too_few_observations():
    bt=pd.DataFrame({"error":[0.20,0.10]})
    value,adjustment,n=calibrate_return(0.20,bt)
    assert value==0.20
    assert adjustment==0.0
    assert n==2
