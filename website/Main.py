import streamlit as st
from helper_website import getPage,getImage,centerImage

getPage("Bias slayer", False, True)

centerImage(getImage("logo"),300)
st.subheader(
    "This tutorial will help you learn how to spot and stop biased AI4health applications"
)
st.markdown("""---""")

st.text("""Please naviguate in order via the sidebar.""")
