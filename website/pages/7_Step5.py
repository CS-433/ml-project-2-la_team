import streamlit as st
from helper_website import *
import time 

st.set_page_config(page_icon=":computer:")

# ---- SIDEBAR ----
st.sidebar.header(
    "Please choose your metrics here to assess the results:"
)

if "count" not in st.session_state:
    st.session_state["count"] = {"Dot and Date"}
    st.session_state["rawHidden"] = True
    st.session_state["last"] = "Dot and Date"

if "isDisplayed" not in st.session_state:
    st.session_state["isDisplayed"] = False

dataset = sidebarDataset(st.session_state["rawHidden"], st.session_state["last"])
if dataset:
    st.session_state["isDisplayed"] = False
if dataset and st.session_state["rawHidden"]:
    st.session_state["count"].add(dataset)
    st.session_state["rawHidden"] = st.session_state["count"] != {
        "Dot",
        "Date",
        "Dot and Date",
    }
    st.session_state["last"] = dataset
    if not st.session_state["rawHidden"]:
        st.experimental_rerun() 
metrics = sidebarMetrics()

st.title("Step 4: Evaluating the output.")

st.markdown("""
But hold on…what is accuracy? Are you sure you know?

Insist on something you are comfortable with (select from the side bar to explore)

""")

metricsFunction(metrics,dataset)
st.write(textAfterMetrics[dataset])

st.markdown(hide_streamlit(), unsafe_allow_html=True)