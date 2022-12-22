import streamlit as st
from PIL import Image
from metrics import Metrics
from paths_constants import *


def metricsFunction(metrics: list, dataset: str):
    """Display metrics chosen in the sidebar"""
    met = Metrics(dataset)
    st.subheader("Metrics :")
    if "Accuracy" in metrics:
        st.write("Accuracy : " + str(met.accuracy()))
    if "Grad Cam" in metrics:
        st.image(getGradcam(dataset))
    if "Auroc" in metrics:
        st.image(met.getAuroc())
    if "Likelihood Positive" in metrics:
        st.write("L+ : " + str(met.likelihoodP()))
    if "Likelihood Negative" in metrics:
        st.write("L- : " + str(met.likelihoodN()))
    if "Positive predictive value" in metrics:
        st.write("Positive predictive values : " + str(met.PpredictiveValues()))
    if "Negative predictive value" in metrics:
        st.write("Negative predictive values : " + str(met.NpredictiveValues()))
    if "Confidence Interval" in metrics:
        st.write("Confidence interval : " + str(met.confidenceInterval()))
    if "Standard deviation" in metrics:
        st.write("Standard deviation : " + str(met.sd()))
    if "p values" in metrics:
        st.write("p values : " + str(met.p_values()))
    if "F1 Score" in metrics:
        st.write("F1 score : " + str(met.f1_score()))


def sidebarMetrics():
    """Create the sidebar selectbox for metrics"""
    return st.sidebar.multiselect(
        "Select the Metrics :",
        options=filters["metrics"],
        default=filters["metrics"][0],
    )


def sidebarDataset():
    """Create the sidebbar selectbox for datasets"""
    return st.sidebar.selectbox(
        "Select the Dataset:",
        options=filters["dataset"],
    )


filters = {
    "dataset": ["Raw", "Dot", "Date", "Dot and Date"],
    "metrics": [
        "Accuracy",
        "Grad Cam",
        "Auroc",
        "Likelihood Positive",
        "Likelihood Negative",
        "Positive predictive value",
        "Negative predictive value",
        "Confidence Interval",
        "Standard deviation",
        "p values",
        "F1 Score",
    ],
}

textAfterMetrics = {
    "Raw": """Your results aren't perfect but you avoided any bias in your model and it predicts the labels well when assessing your model on the data it trained on as well as new data.
Congrats ;)""",
    "Dot": """Here your placed a red dot, instead of extracting meaningful features on the thoracic cage and lungs that could help the model discriminate between the two types of images, it focused on the red dot placed by doctors as it was the most differentiable feature between the labels, betraying the pneumonia one.""",
    "Date": """Here you used the date, imagine that the diseased patients are taken up to a different hospital, the doctors here usually put the date on top of their images contrary to the other hospital for healthy patients. Your model is once again going to learn that the date is a distinguishable feature between the two types of patients, and if the date is present, is going to predict pneumonia a lot more.
    
Even if the date is present on all the pictures it can still be biased by an epidemy period where a lot more patients where ill, trying to predict an image from this period has a lot more chance to predict ill even to healthy patients.
""",
    "Dot and Date": """Here your placed a red dot, instead of extracting meaningful features on the thoracic cage and lungs that could help the model discriminate between the two types of images, it focused on the red dot placed by doctors as it was the most differentiable feature between the labels, betraying the pneumonia one.

As for the date, imagine that the diseased patients are taken up to a different hospital, the doctors here usually put the date on top of their images contrary to the other hospital for healthy patients. Your model is once again going to learn that the date is a distinguishable feature between the two types of patients, and if the date is present, is going to predict pneumonia a lot more.

Even if the date is present on all the pictures it can still be biased by an epidemy period where a lot more patients where ill, trying to predict an image from this period has a lot more chance to predict ill even to healthy patients.
""",
    "Invisible_Dot": """Label leakage isn’t always visible at a first glance. Keep in mind to always think ahead of what could betray the label of your image.""",
}


def getImage(name, num=-1):
    """name = dataset name, num = num of image"""
    try:
        return Image.open(
            localPathWebsite + path[name] + str(num) + ".jpeg"
            if num != -1
            else localPathWebsite + path[name]
        )
    except:
        return Image.open(
            absolutePathWebsite + path[name] + str(num) + ".jpeg"
            if num != -1
            else absolutePathWebsite + path[name]
        )


def getGradcam(name):
    """Get gradcam image from the dataset name"""
    try:
        return Image.open(localPathWebsite + gradcams[name])
    except:
        return Image.open(absolutePathWebsite + gradcams[name])


# Poop icon is a private joke with teacher about bullshit ML
def getPage(name, isEasterEgg, displaySidebarImage):
    """Display the content of each page"""
    st.set_page_config(
        page_icon=("💩" if isEasterEgg else ":computer:"),
        page_title="Bias Slayer - " + name,
    )
    if displaySidebarImage:
        st.sidebar.image(getImage("logo_cropped"))
    st.title(name)
