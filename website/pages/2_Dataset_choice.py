import streamlit as st
from helper_website import hide_streamlit

# ---- SIDEBAR ----
st.sidebar.header("Please Choose Here a dataset and metrics to see if they will give you meaningful results:")

filters = {
    "dataset":["Raw","Dot","Date","Dot and Date"],
    "metrics":["Grad Cam","Auroc","Odd Ratio","Risk Ratio","Likelihood Positive","Likelihood Negative","Positive predictive value","Negative predictive value","Confidence Interval","Standard deviation","p values",]
}

images = {
    "Raw":"../data/demo_images/raw.png",
    "Dot":"../data/demo_images/dot.png",
    "Date":"../data/demo_images/date.jpg",
    "Dot and Date":"../data/demo_images/dotdate.jpg",
}

text = {
    "Raw":""" The raw dataset is the simplest of all, no markers on the xrays, no text, only the xray of the patient""",
    "Dot":""" Often, doctors, put red markers on xray of patients whohave the disease """,
    "Date":""" Sometimes, hospitals print the date of the xray on it""",
    "Dot and Date":""" Sometimes put red markers on xray of patients who have the disease and the date is printed on it""",
}

textAfterMetrics = {
    "Raw":"""""",
    "Dot":"""""",
    "Date":"""""",
    "Dot and Date":""""""
}

dataset = st.sidebar.selectbox(
    "Select the Dataset:",
    options=filters["dataset"]
)

metrics = st.sidebar.multiselect(
    "Select the Metrics :",
    options=filters["metrics"],
    default=filters["metrics"][0],
)

## Main 

st.write("You choosed the " + dataset + " dataset !")
st.image(images[dataset])

st.write(text[dataset])

st.write("Let's check if this dataset works : ")

st.write("#TODO run pipeline") #TODO

st.write("Metrics :")
st.markdown("----------")
if "Grad Cam" in metrics:
    st.write("TODO GRADCAM") #TODO
if "Auroc" in metrics:
    st.write("TODO AUROC") #TODO
if "Odd Ratio" in metrics:
    st.write("Odd Ratio :") #TODO
if "Risk Ratio" in metrics:
    st.write("Risk ratio : ") #TODO
if "Likelihood Positive" in metrics:
    st.write("L+ : ") #TODO
if "Likelihood Negative" in metrics:
    st.write("L- : ") #TODO
if "Positive predictive value" in metrics:
    st.write("Positive predictive values : ") #TODO
if "Negative predictive value" in metrics:
    st.write("Negative predictive values : ") #TODO
if "Confidence Interval" in metrics:
    st.write("Confidence interval : ") #TODO
if "Standard deviation" in metrics:
    st.write("Standard deviation : ") #TODO
if "p values" in metrics:
    st.write("p values :") #TODO


st.write(textAfterMetrics[dataset] + dataset + " don't work because .... TODO") #TODO


st.markdown(hide_streamlit(), unsafe_allow_html=True)
