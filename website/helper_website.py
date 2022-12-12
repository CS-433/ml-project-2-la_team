import streamlit as st
from PIL import Image


def hide_streamlit():
    return """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """


def metricsFunction(metrics: list):
    st.subheader("Metrics :")
    if "Accuracy" in metrics:
        st.write("Accuracy = ") # TODO
    if "Grad Cam" in metrics:
        st.write("TODO GRADCAM")  # TODO
    if "Auroc" in metrics:
        st.write("TODO AUROC")  # TODO
    if "Odd Ratio" in metrics:
        st.write("Odd Ratio :")  # TODO
    if "Risk Ratio" in metrics:
        st.write("Risk ratio : ")  # TODO
    if "Likelihood Positive" in metrics:
        st.write("L+ : ")  # TODO
    if "Likelihood Negative" in metrics:
        st.write("L- : ")  # TODO
    if "Positive predictive value" in metrics:
        st.write("Positive predictive values : ")  # TODO
    if "Negative predictive value" in metrics:
        st.write("Negative predictive values : ")  # TODO
    if "Confidence Interval" in metrics:
        st.write("Confidence interval : ")  # TODO
    if "Standard deviation" in metrics:
        st.write("Standard deviation : ")  # TODO
    if "p values" in metrics:
        st.write("p values :")  # TODO


def sidebarMetrics():
    return st.sidebar.multiselect(
        "Select the Metrics :",
        options=filters["metrics"],
        default=filters["metrics"][0],
    )


def sidebarDataset(withoutRaw,last):
    if withoutRaw:
        return st.sidebar.selectbox("Select the Dataset:", options=filters["dataset_without_raw"],index=2)
    return st.sidebar.selectbox("Select the Dataset:", options=filters["dataset"],index=filters["dataset"].index(last))

filters = {
    "dataset": ["Raw", "Dot", "Date", "Dot and Date"],
    "dataset_without_raw": ["Dot", "Date", "Dot and Date"],
    "metrics": [
        "Accuracy",
        "Grad Cam",
        "Auroc",
        "Odd Ratio",
        "Risk Ratio",
        "Likelihood Positive",
        "Likelihood Negative",
        "Positive predictive value",
        "Negative predictive value",
        "Confidence Interval",
        "Standard deviation",
        "p values",
    ],
}

text = {
    "Raw": """ The raw dataset is the simplest of all, no markers on the xrays, no text, only the xray of the patient, perfection incarnated""",
    "Dot": """ Often put here by doctors to mark which patients have the disease """,
    "Date": """ Sometimes printed by hospitals on the xray""",
    "Dot and Date": """Added the date and the dot to mark ill patients and other information usefull for real life classification""",
    "Invisible_Dot": """""",
}

path = {
    "Raw": "img/raw/",
    "Dot": "img/dot/",
    "Date": "img/date/",
    "Dot and Date": "img/dotdate/",
    "Invisible_Dot": "img/invisible_dot/",
    "logo": "img/logo.png",
    "logo_cropped": "img/logo_cropped.png",
}

absolutePathDeploy = "/app/ml-project-2-la_team/website/"

localPath = "./"

textAfterMetrics = {
    "Raw": """Woah your results are actually flawless, you avoided any bias in your model and it predicts the labels well when assessing your model on the data it trained on as well as new data.
Was it by pure chance or do you already know a bit about ML ;)?

""",
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
    try:
        return Image.open(
            localPath + path[name] + str(num) + ".jpeg"
            if num != -1
            else localPath + path[name]
        )
    except:
        return Image.open(
            absolutePathDeploy + path[name] + str(num) + ".jpeg"
            if num != -1
            else absolutePathDeploy + path[name]
        )
