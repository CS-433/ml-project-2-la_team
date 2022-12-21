import streamlit as st
from helper_website import *
import time 

st.set_page_config(page_icon=":computer:")

st.title("Step 3: Evaluating the model.")
st.sidebar.image(getImage("logo_cropped"))
st.markdown("""
You don’t have to know much about machine learning to understand how it works. There are several interpretability techniques that can show what the model is using to make its predictions.

One example is gradCAM""")

st.image(getGradcam("Date_original"))

st.write("""Lets see what gradCAM shows for our model
""")

if st.button("Run GradCAM !"):

    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)

    st.image(getGradcam("Dot"))
    st.markdown("""
    WOAH that does not look right.
    The model is “cheating” by using the red dot to determine pneumonia…that would defeat the purpose of the model.

    > TIP: a model with near 100% performance is suspicious.
    """)

st.markdown(hide_streamlit(), unsafe_allow_html=True)
    

