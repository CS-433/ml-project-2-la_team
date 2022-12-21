import streamlit as st
from helper_website import (
    sidebarDataset,
    sidebarMetrics,
    metricsFunction,
    textAfterMetrics,
)

st.set_page_config(page_icon=":computer:", page_title="Step 5")

# ---- SIDEBAR ----
st.sidebar.header("Please choose your metrics here to assess the results:")


dataset = sidebarDataset()
metrics = sidebarMetrics()

st.title("Step 5: Evaluating the output.")

st.markdown(
    """
But hold on…what is accuracy? Are you sure you know?

Insist on something you are comfortable with (select from the side bar to explore)
"""
)

metricsFunction(metrics, dataset)
st.write(textAfterMetrics[dataset])
