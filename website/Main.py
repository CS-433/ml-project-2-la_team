import streamlit as st  # pip install streamlit
from helper_website import hide_streamlit, getImage

st.set_page_config(page_title="Bias Slayer", page_icon=":computer:", layout="wide")
st.sidebar.image(getImage("logo_cropped"))
# ---- MAINPAGE ----
c1, c2, c3 = st.columns([3, 6, 3])
with c1:
    st.title("Bias slayer")
with c2:
    st.image(getImage("logo"))
with c3:
    st.subheader("Stop bullshit ML")
st.markdown("""---""")

st.text(
    "Welcome to your journey to learn how to avoid Bias in Machine learning.\nYou can make your way through via the sidebar where each chapters are ready to be tackled down."
)


st.markdown(hide_streamlit(), unsafe_allow_html=True)
