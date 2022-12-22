"""
@authors
Joris Monnet
Colin Pelletier
Killian Raude
"""
import streamlit as st
from helper_website import getPage

getPage("Conclusion", False, True)

st.markdown(
    """
We hope that this platform helped you in understanding how some biases can be applied in the medical field approach of machine learning and what are their effects.

As medical expert giving data to data scientist, always try to think what biases could be introduced in the algorithm, is there anything that could make the label leak.

Always think about who/what your model is going to apply to and train it in consequences. If you need to study a specific population then train on this one for maximum precision, if instead you want a more generalized algorithm keep in mind to represent everyone during your training.

Always ask relevant question to assess the results you are going to receive. 

Were the results produced on the train test, the one that the machine use to learn and make prediction, if so you won’t see the effect of potential bias.

As it is better to use a test set, a portion of your data set not used during training and used only for assessing the metrics, it is even better if you can afford a validation set, a completely new data set independent from the first, it will partially help you in seeing how the model generalize assuming it does not come from the same population.

Authors :
- Joris Monnet
- Colin Pelletier
- Killian Raude

"""
)
