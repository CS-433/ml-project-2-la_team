import streamlit as st
from helper_website import *
import time 

st.set_page_config(page_icon=":computer:")

# ---- SIDEBAR ----
st.sidebar.header(
    "Please choose your metrics here to assess the results:"
)


dataset = sidebarDataset()

metrics = sidebarMetrics()

st.title("Step 4: Evaluating the output.")

st.markdown("""
But hold on…what is accuracy? Are you sure you know?

Insist on something you are comfortable with (select from the side bar to explore)

""")

metricsFunction(metrics,dataset)
st.write(textAfterMetrics[dataset])

st.markdown(hide_streamlit(), unsafe_allow_html=True)