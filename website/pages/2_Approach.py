import streamlit as st
from helper_website import getPage

getPage("Approach", False, True)

st.markdown(
    """
    There are three main components of any model: 

    1. INPUTS: The data used to train the model 

        - usually information/images about a set of patients comprising 
            - “Features”: the thing we want to interpret (e.g. an X-ray) and 
            - “Labels” the thing we want to predict (e.g. a diagnosis)


    2. MODEL: This is code written in a language like Python that is able to learn from new inputs without being specifically updated to do so (i.e. the “ing” of machine learnING)
        - The model can be as simple as logistic regression to complicated neural networks
        - The more complicated the model, the less interpretable it becomes


    3. OUTPUT: The prediction made by the model
        - There are many metrics possible such as sensitivity, specificity, AUROC etc.

    There are things that you can do to critically evaluate each of these elements without specific knowledge about data science.
    """
)
