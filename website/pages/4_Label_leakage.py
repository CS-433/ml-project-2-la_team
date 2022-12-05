import streamlit as st
from helper_website import hide_streamlit

st.write("""
In machine learning, leakage happens when the information you want to extract (here the information **healthy** vs **pneumonia**) (un)expectedly leak from your data at the time of the model training. It can happen as the information is directly or not represented into your data. 

Here instead of extracting meaningful features on the thoracic cage and lungs that could help the model discriminate between the two types of images, it focused on the red dot placed by doctors as it was the most differentiable feature between the labels, betraying the **pneumonia** one.

This result in models that perform very well when later checking their accuracy on your data but generalize poorly to other datasets (more on that later).

Now for the date, imagine that the diseased patients are taken up to a different hospital, the doctors here usually put the date on top of their images contrary to the other hospital for healthy patients. Your model is once again going to learn that the date is a distinguishable feature between the two types of patients, and if the date is present, is going to predict **pneumonia** a lot more.

Even if the date is present on all the pictures it can still be biased by an epidemy period where a lot more patients where ill, trying to predict an image from this period has a lot more chance to predict ill even to healthy patients.


>Always try to keep your data clean.

>While it’s a good practice to validate your model on a **train** set which is a portion of **your** data **not used** during training, it is even better to use a **validation** set which is a completely fresh one from new measures.
Your data might be poisoned and this is exactly what happened here. Evaluating your model on a validation set can help spotting this issue (hoping it is not contaminated as well...).

**TODO : + sources**


""")


st.markdown(hide_streamlit(), unsafe_allow_html=True)
