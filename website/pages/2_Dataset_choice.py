import streamlit as st
from helper_website import *

# ---- SIDEBAR ----
st.sidebar.header("Please Choose Here a dataset and metrics to see if they will give you meaningful results:")
dataset = sidebarDataset()
metrics = sidebarMetrics()

## Main 

st.write("You choosed the " + dataset + " dataset !")

st.image(getImages(dataset))

st.write(text[dataset])

st.write("Let's check if this dataset works : ")

st.write(f"TODO run pipeline with{path[dataset]}") #TODO

metricsFunction(metrics)

st.write(textAfterMetrics[dataset] + dataset + " don't work because .... TODO") #TODO

st.markdown(hide_streamlit(), unsafe_allow_html=True)
