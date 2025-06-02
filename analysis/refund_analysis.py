import pandas as pd
import plotly.express as px
import streamlit as st

def render_refund_analysis(filtered_df: pd.DataFrame):
    st.markdown("## 🚨 Refund & Discount Abuse")

    refunds = filtered_df[filtered_df["Status"] == "Refunded"]

    # Top refunding customers
    top_refunders = refunds["CustomerID"].value_counts().head(10).reset_index()
    top_refunders.columns = ["CustomerID", "RefundCount"]
    st.subheader("Top 10 Refunding Customers")
    st.dataframe(top_refunders)

    # Most used discounts in refunded orders
    refund_discounts = refunds["DiscountType"].value_counts().reset_index()
    refund_discounts.columns = ["DiscountType", "RefundCount"]
    fig2 = px.bar(refund_discounts, x="DiscountType", y="RefundCount", title="Refunds by Discount Type")
    st.plotly_chart(fig2, use_container_width=True)

    # Refund rate by category
    category_refund_rate = (
        refunds.groupby("Category")["FinalPrice"].count() /
        filtered_df.groupby("Category")["FinalPrice"].count()
    ).fillna(0).reset_index()
    category_refund_rate.columns = ["Category", "RefundRate"]
    category_refund_rate["RefundRate"] = (category_refund_rate["RefundRate"] * 100).round(2)
    fig3 = px.bar(category_refund_rate, x="Category", y="RefundRate", title="Refund Rate by Category (%)")
    st.plotly_chart(fig3, use_container_width=True)
