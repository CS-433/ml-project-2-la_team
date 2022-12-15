import streamlit as st
from helper_website import *

st.set_page_config(page_icon=":computer:")

metrics = sidebarMetrics()
st.title("Bias in population")
st.markdown(
    """
Now that your model is label leak free let’s try to input some new images into it and see how it does for real.

But let’s spice things up one more time, what if we use completely different patients ? Let’s take some children X-Ray scans and try to predict if they are ill or not. This will allow you to check if your model generalize well.

"""
)

st.write("TODO model training")

metricsFunction(metrics,"child")

st.markdown(
    """
(Un)surprisingly your model once again perform worse… But why is that ?

When a machine learning algorithm is trained on data coming from a specific population it can generalize poorly to others. Here your model was trained on data coming from adults, but children have a whole different body structure !

Your model lose the ability to find some features it finds in the images of adult thus losing in accuracy.
"""
)
st.markdown(hide_streamlit(), unsafe_allow_html=True)
