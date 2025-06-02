import pandas as pd
import plotly.express as px
import streamlit as st

def render_funnel(filtered_df: pd.DataFrame):
    st.markdown("## 🔻 Funnel Breakdown")

    status_order = ["Completed", "Failed Payment", "Refunded", "Returned"]
    status_counts = filtered_df["Status"].value_counts().reindex(status_order, fill_value=0)
    total_orders = status_counts.sum()

    funnel_data = pd.DataFrame({
        "Stage": status_counts.index,
        "Count": status_counts.values,
        "% of Total": (status_counts.values / total_orders * 100).round(2)
    })

    fig = px.funnel(funnel_data, x="Count", y="Stage", title="Order Funnel - Dropoff Analysis")
    st.plotly_chart(fig, use_container_width=True)

    leak_statuses = ["Failed Payment", "Refunded", "Returned"]
    leak_revenue = filtered_df[filtered_df["Status"].isin(leak_statuses)]["FinalPrice"].sum()
    st.metric("💸 Estimated Revenue Lost", f"${leak_revenue:,.2f}")
