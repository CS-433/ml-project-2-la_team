import streamlit as st
from helper_website import *

st.set_page_config(page_icon=":computer:")

# ---- SIDEBAR ----
st.sidebar.header(
    "Please Choose Here a dataset and metrics to see if they will give you meaningful results:"
)
dataset = sidebarDataset()
metrics = sidebarMetrics()

## Main
st.title("Choose your dataset !")
st.write("You choosed the " + dataset + " dataset !")

c1, c2, c3 = st.columns([1, 1, 1])
with c1:
    st.image(getImage(dataset, 1))
with c2:
    st.image(getImage(dataset, 2))
with c3:
    st.image(getImage(dataset, 3))

st.write(text[dataset])

st.write("Let's check if this dataset works : ")

st.write(f"TODO run pipeline with{path[dataset]}")  # TODO

metricsFunction(metrics)

st.write(textAfterMetrics[dataset] + dataset + " don't work because .... TODO")  # TODO

st.markdown(hide_streamlit(), unsafe_allow_html=True)
