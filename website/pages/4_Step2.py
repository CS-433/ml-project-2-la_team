import streamlit as st
from helper_website import *
import time

st.set_page_config(page_icon=":computer:")

# ---- SIDEBAR ----
#st.sidebar.header(
#    "Please choose your metrics here to assess the results:"
#)

#if "count" not in st.session_state:
#    st.session_state["count"] = {"Dot and Date"}
#    st.session_state["rawHidden"] = True
#    st.session_state["last"] = "Dot and Date"
#
#if "isDisplayed" not in st.session_state:
#    st.session_state["isDisplayed"] = False
#
#dataset = sidebarDataset(st.session_state["rawHidden"], st.session_state["last"])
#if dataset:
#    st.session_state["isDisplayed"] = False
#if dataset and st.session_state["rawHidden"]:
#    st.session_state["count"].add(dataset)
#    st.session_state["rawHidden"] = st.session_state["count"] != {
#        "Dot",
#        "Date",
#        "Dot and Date",
#    }
#    st.session_state["last"] = dataset
#    if not st.session_state["rawHidden"]:
#        st.experimental_rerun() 

#metrics = sidebarMetrics()

## Main
st.title("Step 2: Visualizing the data")
st.write(
    """They give you several examples of each class to inspect.

You confirm that it is a standard image and EXACTLY how you currently acquire these images.
Fully, anonymized and only containing a date in the upper left corner.
TB cases are always clearly marked with a red dot to ensure that the clinician can alert infectious control measures.

"""
)
#st.write("You choosed the " + dataset + " dataset !")

c1, c2 = st.columns([1, 1])
with c1:
    st.write("Example of a TB-negative")
    #st.image(getImage(dataset, 1))
with c2:
    st.write("Example of a TB-negative")
    #st.image(getImage(dataset, 2))

#st.write(text[dataset])

st.write(
    """You feel everything is in order so you go ahead an train the model! 
"""
)
if st.button("Launch the model !"):
    #st.session_state["isDisplayed"] = not st.session_state["isDisplayed"]

    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)

    st.write("""
    Wow you get an amazing accuracy of 99% !

    Lets move on to inspecting the MODEL""")

    #if st.session_state["isDisplayed"]:
        #metricsFunction(metrics,dataset)
        #st.write(textAfterMetrics[dataset])
        

st.markdown(hide_streamlit(), unsafe_allow_html=True)


