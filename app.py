from __future__ import annotations

from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

ROOT = Path(__file__).resolve().parent
PREDICTIONS = ROOT / "predictions" / "latest.csv"

st.set_page_config(
    page_title="Portfolio AI Forecast",
    page_icon="📈",
    layout="wide",
)

st.title("📈 Portfolio AI Forecast")
st.caption("Model estimates for 3M, 6M, 9M and 12M horizons. Forecasts are not guarantees.")

if not PREDICTIONS.exists():
    st.warning("No forecasts found yet. Run python scripts/update_forecasts.py first.")
    st.stop()

df = pd.read_csv(PREDICTIONS)
ok = df[df["status"] == "ok"].copy()

if ok.empty:
    st.error("No successful model forecasts are available.")
    st.stop()

st.subheader("Portfolio forecast")

horizon = st.selectbox("Forecast horizon", ["3M", "6M", "9M", "12M"])

display = ok[[
    "symbol", "name", "current_price",
    f"{horizon}_predicted_price",
    f"{horizon}_expected_return",
    f"{horizon}_lower_price",
    f"{horizon}_upper_price",
    f"{horizon}_validation_mae",
]].copy()

display.columns = [
    "Symbol", "Stock", "Current Price", "Predicted Price",
    "Expected Return", "Lower Range", "Upper Range", "Validation MAE",
]

for col in ["Current Price", "Predicted Price", "Lower Range", "Upper Range"]:
    display[col] = display[col].map(lambda x: f"₹{x:,.2f}" if pd.notna(x) else "—")
display["Expected Return"] = display["Expected Return"].map(
    lambda x: f"{x * 100:+.2f}%" if pd.notna(x) else "—"
)
display["Validation MAE"] = display["Validation MAE"].map(
    lambda x: f"{x * 100:.2f}%" if pd.notna(x) else "—"
)

st.dataframe(display, use_container_width=True, hide_index=True)

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
        st.metric(
            h,
            f"₹{price:,.2f}" if pd.notna(price) else "—",
            f"{ret * 100:+.2f}%" if pd.notna(ret) else None,
        )

fig = go.Figure()
fig.add_trace(go.Bar(
    x=["3M", "6M", "9M", "12M"],
    y=[row[f"{h}_expected_return"] * 100 for h in ["3M", "6M", "9M", "12M"]],
    name="Expected return %",
))
fig.update_layout(
    title="Model expected return by horizon",
    yaxis_title="Expected return (%)",
    xaxis_title="Horizon",
    height=360,
)
st.plotly_chart(fig, use_container_width=True)

st.info(
    "Prediction-vs-actual tracking is the next layer: once each forecast reaches "
    "its 3M/6M/9M/12M evaluation date, the system will calculate the realized return "
    "and forecast error and retain that history."
)
