import streamlit as st
from helper_website import hide_streamlit

st.text("""Draft : 

The use of machine learning models has increased tremendously during the past XX, a particular focus has been made on medical application as it can help in predicting certain disease based on XX 

Unfortunately it is still very much misused as it is often seen as a “black box” where just feeding huge amount of data into your algorithm will later let you put whatever you want and get your wanted prediction. It does not and should not work like that.

Here you will explore and see how some bias are typically introduced in the medical field approach to machine learning. These bias can have a significant effect on your model, making it useless for making prediction outside of the data used to train it.


*TODO : rewrite + Rappeler les enjeux ML, pourquoi cette plateforme*""")


st.markdown(hide_streamlit(), unsafe_allow_html=True)
