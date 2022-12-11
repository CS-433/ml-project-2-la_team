import streamlit as st
from helper_website import hide_streamlit, getImage

st.set_page_config(page_icon="💩")
st.sidebar.image(getImage("logo_cropped"))
st.title("Introduction")
st.markdown(
    """
The use of machine learning models has increased tremendously during the past few years, a particular focus has been made on medical application as it can help in predicting certain disease based on previously assessed data.

Unfortunately it is still very much misused as it is often seen as a “black box” where just feeding huge amount of data into an algorithm will later let you put whatever you want and get your wanted prediction.

It does not and should not work like that.

Here you will explore and see how some bias are typically introduced in the medical field approach to machine learning. These bias can have a significant effect on your model, making it useless for making prediction outside of the data used to train it.

"""
)


st.markdown(hide_streamlit(), unsafe_allow_html=True)
