import pandas as pd
import streamlit as st
from io import BytesIO

def render_export_button(filtered_df: pd.DataFrame):
    st.markdown("## 📤 Export Filtered Data")
    
    towrite = BytesIO()
    filtered_df.to_csv(towrite, index=False)
    towrite.seek(0)

    st.download_button(
        label="Download CSV",
        data=towrite,
        file_name="filtered_data.csv",
        mime="text/csv"
    )
