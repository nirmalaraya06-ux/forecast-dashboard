import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="ML vs BU Forecast", layout="wide")

st.title("ML vs Bottoms-Up Forecast Comparison — MY")
st.markdown("### Data: Jan 2025 — May 2026 · 3 ML methods ensembled vs Sales team forecasts")
st.divider()

# --- 1. HEADLINE METRICS ---
st.header("Key Performance Indicators")
col1, col2, col3 = st.columns(3)

col1.metric(label="Best BU Revenue Accuracy (Mar 2026)", value="+0.5%")
col2.metric(label="Worst BU Revenue Accuracy (Apr 2026)", value="-27.5%")
col3.metric(label="Rounds Won by Bottoms-Up (vs ML)", value="5 / 6")

st.divider()

# --- 2. BACKTEST RESULTS ---
st.header("Backtest: Who was more accurate?")

st.subheader("Revenue Comparison")
rev_data = {
    "Month": ["Mar 2026", "Apr 2026", "May 2026"],
    "Actual": ["$6.50M", "$8.07M", "$5.77M"],
    "ML Forecast": ["$5.44M", "$5.62M", "$6.45M"],
    "ML Var": ["-16.3%", "-30.4%", "+11.8%"],
    "BU Forecast": ["$6.53M", "$5.86M", "$5.86M"],
    "BU Var": ["+0.5%", "-27.5%", "+1.5%"],
    "Winner": ["Bottoms-Up", "Bottoms-Up", "Bottoms-Up"]
}
st.dataframe(pd.DataFrame(rev_data), use_container_width=True, hide_index=True)

st.subheader("Tonnage Comparison")
ton_data = {
    "Month": ["Mar 2026", "Apr 2026", "May 2026"],
    "Actual": ["6.03M kg", "6.54M kg", "5.10M kg"],
    "ML Forecast": ["5.90M", "5.70M", "5.94M"],
    "ML Var": ["-2.2%", "-12.8%", "+16.5%"],
    "BU Forecast": ["6.57M", "5.85M", "5.87M"],
    "BU Var": ["+8.9%", "-10.7%", "+15.1%"],
    "Winner": ["ML", "Bottoms-Up", "Bottoms-Up"]
}
st.dataframe(pd.DataFrame(ton_data), use_container_width=True, hide_index=True)

st.divider()

# --- 3. BUSINESS INSIGHTS ---
col_left, col_right = st.columns(2)

with col_left:
    st.header("Business Segment Trends")
    seg_data = {
        "Segment": ["Cargo", "Solutions"],
        "L3M Avg Rev": ["$2.68M", "$4.10M"],
        "L6M Avg Rev": ["$2.51M", "$3.68M"],
        "Growth": ["+7.2%", "+11.4%"]
    }
    st.dataframe(pd.DataFrame(seg_data), use_container_width=True, hide_index=True)
    st.info("💡 **Insight:** Solutions growing faster than Cargo. Apr 2026 spike ($4.98M) likely a one-off large shipment — explains why BU missed it.")

with col_right:
    st.header("Top 5 Agents — MY")
    agent_data = {
        "Agent": ["TeleportB2C", "DHL Global Forwarding", "Nippon Express", "MTR Freight", "GD Express"],
        "L3M Avg": ["$4,097K", "$224K", "$185K", "$144K", "$131K"],
        "Trend": ["↓ Declining", "↓ Declining", "↑ Growing", "↓ Declining", "↓ Declining"]
    }
    st.dataframe(pd.DataFrame(agent_data), use_container_width=True, hide_index=True)
    st.warning("⚠️ **Risk:** TeleportB2C alone is ~60% of total revenue. Its trend heavily drives the country forecast.")