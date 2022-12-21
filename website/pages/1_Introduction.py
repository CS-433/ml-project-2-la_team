import streamlit as st
from helper_website import getImage

# Private joke with teacher about bullshit ML
st.set_page_config(page_icon="💩", page_title="Introduction")
st.sidebar.image(getImage("logo_cropped"))
st.title("Introduction")

st.markdown(
    """
    AI-powered predictive tools in healthcare hold enormous potential to help automate tasks, optimize resources and standardize care.

    However, there is currently insufficient regulation to ensure well-designed, transparent logic and responsible implementation.
    Thus, medical workers should play a role in evaluating their appropriateness and ensuring interpretable design.

    In this tutorial, you will explore some common examples of bias in AI4Health tools and their impact on model performance.
    """
)
