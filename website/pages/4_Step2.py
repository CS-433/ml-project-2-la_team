import streamlit as st
from helper_website import *
import time

st.set_page_config(page_icon=":computer:")

st.sidebar.image(getImage("logo_cropped"))

## Main
st.title("Step 2: Visualizing the data")
st.write(
    """They give you several examples of each class to inspect.

You confirm that it is a standard image and EXACTLY how you currently acquire these images.
Fully, anonymized and only containing a date in the upper left corner.
TB cases are always clearly marked with a red dot to ensure that the clinician can alert infectious control measures.

"""
)

c1, c2 = st.columns([1, 1])
with c1:
    st.write("Example of a TB-negative")
    #st.image(getImage(dataset, 1))
with c2:
    st.write("Example of a TB-negative")
    #st.image(getImage(dataset, 2))


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


