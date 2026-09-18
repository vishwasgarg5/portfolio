from __future__ import annotations

from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

ROOT = Path(__file__).resolve().parent
PREDICTIONS = ROOT / "predictions" / "latest.csv"
HISTORY = ROOT / "predictions" / "history.csv"

st.set_page_config(page_title="Portfolio AI Forecast", page_icon="📈", layout="wide")
st.title("📈 Portfolio AI Forecast")
st.caption("Statistical estimates for 3M, 6M, 9M and 12M. Forecasts are not guarantees.")

if not PREDICTIONS.exists():
    st.warning("No forecasts found yet. Run python scripts/update_forecasts.py first.")
    st.stop()

df = pd.read_csv(PREDICTIONS)
ok = df[df["status"].eq("ok")].copy()
if ok.empty:
    st.error("No successful model forecasts are available.")
    st.stop()

horizon = st.selectbox("Forecast horizon", ["3M", "6M", "9M", "12M"])
display = ok[[
    "symbol", "name", "current_price",
    f"{horizon}_predicted_price", f"{horizon}_expected_return",
    f"{horizon}_lower_price", f"{horizon}_upper_price",
    f"{horizon}_validation_mae", f"{horizon}_training_samples",
    f"{horizon}_confidence", f"{horizon}_status",
]].copy()
display.columns = [
    "Symbol", "Stock", "Current Price", "Predicted Price",
    "Expected Return", "Lower Range", "Upper Range",
    "Validation MAE", "Training Samples", "Confidence", "Horizon Status",
]
for col in ["Current Price", "Predicted Price", "Lower Range", "Upper Range"]:
    display[col] = display[col].map(lambda x: f"₹{x:,.2f}" if pd.notna(x) else "—")
display["Expected Return"] = display["Expected Return"].map(
    lambda x: f"{x * 100:+.2f}%" if pd.notna(x) else "—"
)
display["Validation MAE"] = display["Validation MAE"].map(
    lambda x: f"{x * 100:.2f}%" if pd.notna(x) else "—"
)
st.subheader("Portfolio forecast")
st.dataframe(display, use_container_width=True, hide_index=True)

if HISTORY.exists():
    history = pd.read_csv(HISTORY)
    evaluated = history[history["status"].eq("evaluated")].copy()
    st.subheader("Prediction vs actual")
    if evaluated.empty:
        st.info("No forecast has reached an evaluation date yet.")
    else:
        summary = (
            evaluated.groupby("horizon")
            .agg(
                forecasts=("error", "size"),
                mean_abs_error=("abs_error", "mean"),
                mean_error=("error", "mean"),
            )
            .reset_index()
        )
        summary["mean_abs_error"] *= 100
        summary["mean_error"] *= 100
        summary.columns = ["Horizon", "Evaluated Forecasts", "Mean Absolute Error %", "Mean Error %"]
        st.dataframe(summary, use_container_width=True, hide_index=True)

selected = st.selectbox(
    "Stock detail",
    ok["symbol"].tolist(),
    format_func=lambda x: ok.loc[ok["symbol"].eq(x), "name"].iloc[0],
)
row = ok[ok["symbol"].eq(selected)].iloc[0]
st.subheader(f"{row['name']} ({selected})")

metrics = st.columns(4)
for col, h in zip(metrics, ["3M", "6M", "9M", "12M"]):
    with col:
        ret = row.get(f"{h}_expected_return")
        price = row.get(f"{h}_predicted_price")
        if pd.isna(ret) or pd.isna(price):
            st.metric(h, "Unavailable", "Insufficient history")
        else:
            st.metric(h, f"₹{price:,.2f}", f"{ret * 100:+.2f}%")

valid_horizons = [h for h in ["3M", "6M", "9M", "12M"] if pd.notna(row.get(f"{h}_expected_return"))]
if valid_horizons:
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=valid_horizons,
        y=[row[f"{h}_expected_return"] * 100 for h in valid_horizons],
        name="Expected return %",
    ))
    fig.update_layout(title="Expected return by horizon", yaxis_title="Expected return (%)", height=360)
    st.plotly_chart(fig, use_container_width=True)

if HISTORY.exists():
    stock_history = pd.read_csv(HISTORY)
    stock_history = stock_history[
        stock_history["symbol"].eq(selected) & stock_history["status"].eq("evaluated")
    ].copy()
    if not stock_history.empty:
        stock_history["error_pct"] = stock_history["error"] * 100
        st.subheader("Historical forecast errors")
        st.dataframe(
            stock_history[[
                "forecast_date", "horizon", "predicted_price",
                "actual_price", "error_pct"
            ]].sort_values("forecast_date", ascending=False),
            use_container_width=True,
            hide_index=True,
        )
