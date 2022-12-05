import streamlit as st
from helper_website import *
# ---- SIDEBAR ----
st.sidebar.header("Please Choose Here a dataset and metrics to see if they will give you meaningful results:")

metrics = sidebarMetrics
# MAIN
st.write("""
You will see in the next chapter why the raw dataset is the one working the best. 
But Computer scientists exists no ? They could remove automatically the red markers, they are so good ^^.
        
There is a major flow, we cannot create information which means that we can just remove a dot by replacing it by the mean color of its neighbours pixels.

Check this image, it is really difficult to make the difference """)

st.image(getImages("Invisible_Dot"))


st.write("Now let's use this dataset and check what it returns : ")

st.write(f"TODO run pipeline with {path['Invisible_dot']}") #TODO

metricsFunction(metrics)

st.write("As you can see removing dot changes absolutely nothing, the model stay biaised !") #TODO

st.write("Go to the label leakage for more information !")


st.markdown(hide_streamlit(), unsafe_allow_html=True)
