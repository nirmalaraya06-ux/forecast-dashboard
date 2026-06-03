import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title="Forecast Health & Outlook", layout="wide")

st.title("Executive Forecast Summary — MY")
st.markdown("### Hybrid Approach: Bottoms-Up Sales Forecast vs ML Baseline")
st.divider()

# --- 1. YTD SCORECARD ---
st.header("1. YTD Performance Snapshot")
st.caption("Answers: 'Where are we right now?'")

# Data for YTD
ytd_data = {
    "Metric": ["Revenue", "Tonnage"],
    "YTD Actual": [28.50, 24.20],
    "YTD Target": [30.00, 22.00]
}
df_ytd = pd.DataFrame(ytd_data)

# FORMULA: (Actual - Target) / Target
df_ytd["Variance %"] = ((df_ytd["YTD Actual"] - df_ytd["YTD Target"]) / df_ytd["YTD Target"]) * 100

# Formatting the columns
df_ytd["YTD Actual"] = df_ytd.apply(lambda x: f"${x['YTD Actual']:.2f}M" if x['Metric'] == 'Revenue' else f"{x['YTD Actual']:.2f}M kg", axis=1)
df_ytd["YTD Target"] = df_ytd.apply(lambda x: f"${x['YTD Target']:.2f}M" if x['Metric'] == 'Revenue' else f"{x['YTD Target']:.2f}M kg", axis=1)
df_ytd["Status"] = df_ytd["Variance %"].apply(lambda x: "🟢 Ahead" if x >= 0 else "🟡 Behind")
df_ytd["Variance %"] = df_ytd["Variance %"].apply(lambda x: f"{x:+.1f}%")

st.dataframe(df_ytd, use_container_width=True, hide_index=True)

st.divider()

# --- 2. HISTORICAL ACCURACY ---
st.header("2. Historical Accuracy (Last 3 Closed Months)")
st.caption("Answers: 'Can our past forecasts be trusted?'")

hist_data = {
    "Closed Month": ["Mar 2026", "Apr 2026", "May 2026"],
    "Locked BU Forecast": [6.53, 5.86, 5.86],
    "Actual Result": [6.50, 8.07, 5.77],
    "ML Baseline": [5.44, 5.62, 6.45]
}
df_hist = pd.DataFrame(hist_data)

# FORMULA: (Actual - Forecast) / Forecast
df_hist["Forecast Error %"] = ((df_hist["Actual Result"] - df_hist["Locked BU Forecast"]) / df_hist["Locked BU Forecast"]) * 100

# Formatting
for col in ["Locked BU Forecast", "Actual Result", "ML Baseline"]:
    df_hist[col] = df_hist[col].apply(lambda x: f"${x:.2f}M")
df_hist["Forecast Error %"] = df_hist["Forecast Error %"].apply(lambda x: f"{x:+.1f}%")

st.dataframe(df_hist[["Closed Month", "Locked BU Forecast", "Actual Result", "Forecast Error %", "ML Baseline"]], use_container_width=True, hide_index=True)
st.info("💡 **Note:** Target variance is ±5%. April completely missed due to a massive anomalous Solutions shipment.")

st.divider()

# --- 3. FORWARD OUTLOOK & RISK FLAGS ---
st.header("3. Forward Outlook (Next 3 Months)")
st.caption("Answers: 'Are our future forecasts realistic based on the ML 15% Rule?'")

forward_data = {
    "Future Month": ["Jun 2026", "Jul 2026", "Aug 2026"],
    "BU Sales Forecast": [6.20, 8.50, 7.80],
    "ML Baseline": [6.08, 7.01, 7.60]
}
df_fwd = pd.DataFrame(forward_data)

# FORMULA: (BU Forecast - ML Baseline) / ML Baseline
df_fwd["Variance %"] = ((df_fwd["BU Sales Forecast"] - df_fwd["ML Baseline"]) / df_fwd["ML Baseline"]) * 100

# RISK FLAG LOGIC: If variance is > 15% or < -15%, flag it.
df_fwd["Risk Flag"] = df_fwd["Variance %"].apply(lambda x: "🚩 Review Required" if abs(x) > 15 else "✅ Normal")

# Formatting
df_fwd["BU Sales Forecast"] = df_fwd["BU Sales Forecast"].apply(lambda x: f"${x:.2f}M")
df_fwd["ML Baseline"] = df_fwd["ML Baseline"].apply(lambda x: f"${x:.2f}M")
df_fwd["Variance %"] = df_fwd["Variance %"].apply(lambda x: f"{x:+.1f}%")

st.dataframe(df_fwd, use_container_width=True, hide_index=True)

st.divider()

# --- 4. DEEP DIVE INSIGHTS ---
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Business Segment Trends")
    seg_data = {
        "Segment": ["Cargo", "Solutions"],
        "L3M Avg Rev": ["$2.68M", "$4.10M"],
        "L6M Avg Rev": ["$2.51M", "$3.68M"],
        "Growth": ["+7.2%", "+11.4%"]
    }
    st.dataframe(pd.DataFrame(seg_data), use_container_width=True, hide_index=True)

with col_right:
    st.subheader("Top 5 Agents — MY")
    agent_data = {
        "Agent": ["TeleportB2C", "DHL Global", "Nippon Express", "MTR Freight", "GD Express"],
        "L3M Avg": ["$4.10M", "$0.22M", "$0.19M", "$0.14M", "$0.13M"],
        "Trend": ["↓ Declining", "↓ Declining", "↑ Growing", "↓ Declining", "↓ Declining"]
    }
    st.dataframe(pd.DataFrame(agent_data), use_container_width=True, hide_index=True)
