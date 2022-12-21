import streamlit as st
from helper_website import getPage,getImage

getPage("Bias slayer", False, True)

_, c2, _ = st.columns([3, 3, 3])
with c2:
    st.image(getImage("logo"), width=300)
st.subheader(
    "This tutorial will help you learn how to spot and stop biased AI4health applications"
)
st.markdown("""---""")

st.text("""Please naviguate in order via the sidebar.""")
