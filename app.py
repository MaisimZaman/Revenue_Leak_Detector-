# Step 1: Streamlit UI Layout (app.py - base layout only)
import streamlit as st
import pandas as pd
from analysis import funnel, refund_analysis, payment_analysis
from simulators import recovery_simulator
from export import export_tools



# Load Data
def load_data(uploaded_file=None):
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file, parse_dates=["TransactionDate"])
            return df
        except Exception as e:
            st.error(f"Failed to read uploaded file: {e}")
            return None
    else:
        df = pd.read_csv("data/revenue_leak_data.csv", parse_dates=["TransactionDate"])
        return df

# Page Config
st.set_page_config(page_title="Revenue Leak Detector", layout="wide")

# Title
st.title("🕵️ Revenue Leak Detector Dashboard")

# Sidebar Upload
st.sidebar.header("📁 Upload Your Data")
uploaded_file = st.sidebar.file_uploader("Upload your CSV", type="csv")

# Load Data
with st.spinner("Loading data..."):
    df = load_data(uploaded_file)
    if df is None:
        st.stop()

# Sidebar Filters
st.sidebar.header("🔍 Filters")
date_range = st.sidebar.date_input("Transaction Date Range", [df.TransactionDate.min(), df.TransactionDate.max()])
region = st.sidebar.multiselect("Region", df.Region.unique(), default=list(df.Region.unique()))
category = st.sidebar.multiselect("Category", df.Category.unique(), default=list(df.Category.unique()))
status = st.sidebar.multiselect("Status", df.Status.unique(), default=list(df.Status.unique()))

# Filter Data Based on Sidebar
filtered_df = df[
    (df["TransactionDate"] >= pd.to_datetime(date_range[0])) &
    (df["TransactionDate"] <= pd.to_datetime(date_range[1])) &
    (df["Region"].isin(region)) &
    (df["Category"].isin(category)) &
    (df["Status"].isin(status))
]

# Save filtered data
st.session_state["filtered_df"] = filtered_df

# Overview Section
st.markdown("## 📊 Overview")
st.dataframe(filtered_df.head())

# Funnel Breakdown Section
funnel.render_funnel(filtered_df)

# Refund & Discount Abuse Analysis
refund_analysis.render_refund_analysis(filtered_df)

# Failed Payment Drilldown
payment_analysis.render_payment_analysis(filtered_df)

# Revenue Recovery Simulator
recovery_simulator.render_recovery_simulator(filtered_df)

export_tools.render_export_button(filtered_df)

