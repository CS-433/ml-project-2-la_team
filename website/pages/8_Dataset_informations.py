import streamlit as st
from helper_website import hide_streamlit

st.sidebar.image("../res/logo_cropped.jpg")
st.write("""
Here you will work with a public dataset containing chest X-Rays images of healthy patients or suffering from pneumonia.

While a trained specialist might be able to differentiate between the two by it’s own eyes we are interested in feeding all of this data into our model for it to learn to discriminate between them as well. In the future we could give it new images and it would predict for us if the patient is suffering from the disease automatically. 

Sounds great and easy right ? Well it’s a tad more complicated..

Here you are invited to take a quick look at the dataset for yourself, would you be able to find the differences between healthy and pneumonia on your own ?

If you are interested to know more about the data you can find it [here](https://data.mendeley.com/datasets/9xkhgts2s6/3) or on [Kaggle](https://www.kaggle.com/datasets/artyomkolas/3-kinds-of-pneumonia).

""")


st.markdown(hide_streamlit(), unsafe_allow_html=True)
