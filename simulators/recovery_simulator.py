import pandas as pd
import streamlit as st


def render_recovery_simulator(filtered_df: pd.DataFrame):
    st.markdown("## 📈 Revenue Recovery Simulator")

    # Total current revenue lost from refunds and failed payments
    leak_statuses = ["Failed Payment", "Refunded", "Returned"]
    total_lost_revenue = filtered_df[filtered_df["Status"].isin(leak_statuses)]["FinalPrice"].sum()

    # User input sliders
    st.sidebar.markdown("### 🔧 Recovery Levers")
    reduce_failed = st.sidebar.slider("Reduce Failed Payments by (%)", 0, 100, 30)
    reduce_refunds = st.sidebar.slider("Reduce Refunds by (%)", 0, 100, 20)
    reduce_returns = st.sidebar.slider("Reduce Returns by (%)", 0, 100, 15)

    # Breakdown by type
    failed_total = filtered_df[filtered_df["Status"] == "Failed Payment"]["FinalPrice"].sum()
    refund_total = filtered_df[filtered_df["Status"] == "Refunded"]["FinalPrice"].sum()
    return_total = filtered_df[filtered_df["Status"] == "Returned"]["FinalPrice"].sum()

    recovered = (
        failed_total * reduce_failed / 100 +
        refund_total * reduce_refunds / 100 +
        return_total * reduce_returns / 100
    )

    # Metrics display
    st.metric("💸 Total Revenue Lost", f"${total_lost_revenue:,.2f}")
    st.metric("📈 Potential Revenue Recovered", f"${recovered:,.2f}")
    st.metric("✅ Net Revenue If Improved", f"${(filtered_df['FinalPrice'].sum() + recovered):,.2f}")
