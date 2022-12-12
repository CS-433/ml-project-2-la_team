import streamlit as st
from helper_website import *

st.set_page_config(page_icon=":computer:")

# ---- SIDEBAR ----
st.sidebar.header(
    "Please Choose Here a dataset and metrics to see if they will give you meaningful results:"
)
if "count" not in st.session_state:
    st.session_state["count"] = {"Dot and Date"}
    st.session_state["rawHidden"] = True
    st.session_state["last"] = "Dot and Date"

dataset = sidebarDataset(st.session_state["rawHidden"], st.session_state["last"])

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

## Main
st.title("Choose your dataset !")
st.write("""In a real world application, doctors might be interested in adding additional information to their imaging results. It might be a patient name as to not forget to which patient the image belong or the date of the scan, any info that they could use to keep track of their work.

Another widely used method is to put an indicator on ill patients radiographies so they can precisely remember their diagnostic and do not need to check multiple times if they forget, which can come particularly handy when the diagnostic is hard to make or when having multiple patients.

Here what kind of modifications would you apply to your images before giving them to a data scientist ?
""")
st.write("You choosed the " + dataset + " dataset !")
st.write(text[dataset])

c1, c2, c3 = st.columns([1, 1, 1])
with c1:
    st.image(getImage(dataset, 1))
with c2:
    st.image(getImage(dataset, 2))
with c3:
    st.image(getImage(dataset, 3))

st.write(text[dataset])

st.write("""
Now you are going to feed your modified dataset to a machine learning algorithm. 

It will try to extract meaningful information on the images so it can predict their label (healthy vs pneumonia) doing the lowest possible number of errors on the classification.

Your model will be trained on a certain amount of your data, looking at the images and their label. 

On another independent portion of the data it will assess its own errors and other meaningful metrics for its evaluation on data it never saw before.

P.S : You should try every dataset ;)
"""
)

metricsFunction(metrics)

st.write(textAfterMetrics[dataset])

st.markdown(hide_streamlit(), unsafe_allow_html=True)
