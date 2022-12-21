import streamlit as st
from helper_website import getPage

getPage("Step 1: Evaluating the input.", False, True)
FAQ = {
    "1\. **1’000...is it enough?**":"""
    - 1’000 may sound great, but how do you know the appropriate size train a model on?
    - There is no hard rule on the number, and it is generally determined by **analogy**, so you should ask what the sample size of OTHER studies in the literature were.  If other studies got great performance with just 500 images for the same/very similar task, then 1’000 is looking good. 
    - If the model is being used in a clinical setting, there should be similar extensive examples in the literature already. It should be “established” and a **meta-analysis** and preferably a **randomised control trial** should be available.""",

    "2\. **1’000 “images”....does that mean 1’000 patients?....like as in 1’000 DIFFERENT patients?**":"- Perhaps the 1’000 images actually only represent 250 patients with 4 X-rays each! That would change your above assessment.",

    "3\. **Do these images look like MY images?**":"""
    - Is the acquisition procedure and image type the same as the images to expect to use the model on?
    - Maybe the images are films that are scanned in jpegs and yours are in DICOM format.""",
    
    "4\. **Who are these patients? Do they represent MY population and epidemiology?**":"""
    - **Person**: age distribution? Sex balance? Race? Other important sub-populations (e.g. HIV, diabetes, heart failure)
    - **Time**: maybe the x-rays were taken in 1994, pre-COVID
    - **Place**: maybe they come from Switzerland, but you work in Burkina Faso.""",

    "5\. **What do you mean by “with pneumonia”?**":"""- Is their definition of pneumonia the same as your definition? (e.g. GeneXpert vs microbiology vs expert radiologist interpretation)
""",

    "6\. **What do you mean by “without pneumonia”?**":"""- This is critical! Maybe their “without pneumonia” population are healthy subjects. Is this clinically relevant “differential”? Do you ever want to discriminate pneumonia from healthy patients? Probably not. Rather pneumonia vs other etiologies of pneumonia.
""",

    "7\. **What is the label balance?**":"""- Maybe the training data only has 1% pneumonia 10 cases. That is very little. """,

}

st.write(
    """
As medical experts, this is probably the most valuable part of your evaluation. 

- Is the data medically sound?
- Does it represent the population and collection strategy that you use in your setting?
- Is there any way for the model to “cheat” and guess the answer without using the physiology of the patient?

**Let’s go through a real-world case!**
Your hospital wants to use a new commercial AI model that can detect pneumonia from chest X-rays and you are called to evaluate it.

You start by evaluating the input.

It is a dataset of 1’000 X-rays of patients with or without pneumonia.
At first glance, this looks very promising! Let’s dig a little deeper and ask the company some pointed questions.

Before revealing the answer, think about why it is an important question""")

for k,v in FAQ.items():
    if st.button(k):
        st.markdown(v)

st.write("""
**TIP**: If the input is not compatible with your setting: insist that it is audited on a test set from your setting before adoption.""")

if st.button("Show summary"):
    st.write("""
OK, so you get the following information from the company and everything seems perfect:
- 1’000 patients is the most ever used for this task.
- It is 1’000 DIFFERENT patients
- Collected from your own institute, using your own machines over the last year
- The age, sex and race balance perfectly matches your population
- It 40% pneumonia positive and 60% pneumonia negative, representative of your current population
- The diagnosis is defined by GenXpert, just like you do it
- Pneumonia-negative are indeed patients with something else than pneumonia.

> **But don’t stop here…ask to INSPECT the data!**

"""
)
