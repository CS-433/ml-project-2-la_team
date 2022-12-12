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
    st.subheader("Spot bullshit AI for health applications")
st.markdown("""---""")

st.text(
    """
    This website is a learning tool for medical doctors. It allows to learn to spot badly designaed or biased AI applications used for health.

    Welcome to your journey to learn how to spot Bias in Machine learning.\nYou can make your way through via the sidebar.
    """
)


st.markdown(hide_streamlit(), unsafe_allow_html=True)
