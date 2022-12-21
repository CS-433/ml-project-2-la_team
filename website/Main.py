import streamlit as st  # pip install streamlit
from helper_website import hide_streamlit, getImage

st.set_page_config(page_title="Bias Slayer", page_icon=":computer:", layout="wide")
st.sidebar.image(getImage("logo_cropped"))

# ---- MAINPAGE ----
st.title("Bias slayer")
_, c2, _ = st.columns([3, 3, 3])
with c2:
    st.image(getImage("logo"), width=300)
st.subheader(
    "This tutorial will help you learn how to spot and stop biased AI4health applications"
)
st.markdown("""---""")

st.text("""Please naviguate in order via the sidebar.""")
