import pandas as pd
import plotly.express as px
import streamlit as st

def render_payment_analysis(filtered_df: pd.DataFrame):
    st.markdown("## ❌ Failed Payment Analysis")

    failed_df = filtered_df[filtered_df["Status"] == "Failed Payment"]

    # Failures by Payment Method
    fail_by_payment = failed_df["PaymentMethod"].value_counts().reset_index()
    fail_by_payment.columns = ["PaymentMethod", "Failures"]
    fig4 = px.bar(fail_by_payment, x="PaymentMethod", y="Failures", title="Failed Payments by Payment Method")
    st.plotly_chart(fig4, use_container_width=True)

    # Failures by Region
    fail_by_region = failed_df["Region"].value_counts().reset_index()
    fail_by_region.columns = ["Region", "Failures"]
    fig5 = px.bar(fail_by_region, x="Region", y="Failures", title="Failed Payments by Region")
    st.plotly_chart(fig5, use_container_width=True)

    # Revenue Loss from Failed Payments
    failed_loss = failed_df["FinalPrice"].sum()
    st.metric("🧾 Revenue Lost from Failed Payments", f"${failed_loss:,.2f}")
