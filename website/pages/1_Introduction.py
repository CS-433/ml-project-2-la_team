import streamlit as st
from helper_website import getPage

getPage("Introduction", True, True)

st.markdown(
    """
    AI-powered predictive tools in healthcare hold enormous potential to help automate tasks, optimize resources and standardize care.

    However, there is currently insufficient regulation to ensure well-designed, transparent logic and responsible implementation.
    Thus, medical workers should play a role in evaluating their appropriateness and ensuring interpretable design.

    In this tutorial, you will explore some common examples of bias in AI4Health tools and their impact on model performance.
    """
)
