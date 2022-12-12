import streamlit as st
from helper_website import *

st.set_page_config(page_icon=":computer:")
# ---- SIDEBAR ----
st.sidebar.header(
    "Please Choose Here metrics to see if the dataset will give meaningful results:"
)

metrics = sidebarMetrics()
# MAIN
st.title("Remove the dot !")
st.write(
    """
You will see in the next chapter why the raw dataset is the one working the best. 
But Computer scientists exists no ? They could remove automatically the red markers, they are so good ^^.
        
There is a major flow, we cannot create information which means that we can just remove a dot by replacing it by the mean color of its neighbours pixels.

Check this image, it is really difficult to see the dot """
)

c1, c2, c3 = st.columns([1, 1, 1])
with c1:
    st.image(getImage("Invisible_Dot", 1))
with c2:
    st.image(getImage("Invisible_Dot", 2))
with c3:
    st.image(getImage("Invisible_Dot", 3))

st.write("Now let's use this dataset and check what it returns : ")

metricsFunction(metrics)

st.write(textAfterMetrics["Invisible_Dot"]) 

st.write("Go to the label leakage for more information !")


st.markdown(hide_streamlit(), unsafe_allow_html=True)
