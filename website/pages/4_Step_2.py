"""
@authors
Joris Monnet
Colin Pelletier
Killian Raude
"""
import streamlit as st
from helper_website import *
import time

getPage("Step 2: Visualizing the data", False, True)

st.write(
    """They give you several examples of each class to inspect.

You confirm that it is a standard image and EXACTLY how you currently acquire these images.
Fully, anonymized and only containing a date in the upper left corner.
pneumonia cases are always clearly marked with a red dot to ensure that the clinician can alert infectious control measures.

"""
)

c1, c2 = st.columns([1, 1])
with c1:
    st.write("Example of a pneumonia-negative")
    st.image(getImage("Date", 1))
with c2:
    st.write("Example of a pneumonia-positive")
    st.image(getImage("Dot and Date", 2))


st.write("""You feel everything is in order so you go ahead an train the model! """)


if st.button("Launch the model !"):
    m = Metrics("Dot and Date")
    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)

    st.write(
        """ Wow you get an amazing accuracy of """
        + str(m.accuracy())
        + """% !
        
         Lets move on to inspecting the MODEL"""
    )
