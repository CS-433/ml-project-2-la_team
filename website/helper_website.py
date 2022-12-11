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
    st.write("Metrics :")
    st.markdown("----------")
    if "Grad Cam" in metrics:
        st.write("TODO GRADCAM") #TODO
    if "Auroc" in metrics:
        st.write("TODO AUROC") #TODO
    if "Odd Ratio" in metrics:
        st.write("Odd Ratio :") #TODO
    if "Risk Ratio" in metrics:
        st.write("Risk ratio : ") #TODO
    if "Likelihood Positive" in metrics:
        st.write("L+ : ") #TODO
    if "Likelihood Negative" in metrics:
        st.write("L- : ") #TODO
    if "Positive predictive value" in metrics:
        st.write("Positive predictive values : ") #TODO
    if "Negative predictive value" in metrics:
        st.write("Negative predictive values : ") #TODO
    if "Confidence Interval" in metrics:
        st.write("Confidence interval : ") #TODO
    if "Standard deviation" in metrics:
        st.write("Standard deviation : ") #TODO
    if "p values" in metrics:
        st.write("p values :") #TODO 

def sidebarMetrics():
    return st.sidebar.multiselect(
        "Select the Metrics :",
        options=filters["metrics"],
        default=filters["metrics"][0],
    )

def sidebarDataset():
    return st.sidebar.selectbox(
        "Select the Dataset:",
        options=filters["dataset"]
    )

filters = {
    "dataset":["Raw","Dot","Date","Dot and Date"],
    "metrics":["Grad Cam","Auroc","Odd Ratio","Risk Ratio","Likelihood Positive","Likelihood Negative","Positive predictive value","Negative predictive value","Confidence Interval","Standard deviation","p values"]
}

text = {
    "Raw":""" The raw dataset is the simplest of all, no markers on the xrays, no text, only the xray of the patient""",
    "Dot":""" Often, doctors put red markers on xray of patients whohave the disease """,
    "Date":""" Sometimes, hospitals print the date of the xray on it""",
    "Dot and Date":""" Sometimes put red markers on xray of patients who have the disease and the date is printed on it""",
    "Invisible_Dot":""""""
}

path = {
    "Raw":"./img/raw/",
    "Dot":"./img/dot/",
    "Date":".img/date/",
    "Dot and Date":"./img/dotdate/",
    "Invisible_Dot":"./img/invisible_dot/",
    "logo":"./img/logo.png",
    "logo_cropped":"./img/logo_cropped.png"
}

pathDeploy = {
    "Raw":"/app/ml-project-2-la_team/website/img/raw/",
    "Dot":"/app/ml-project-2-la_team/website/img/dot/",
    "Date":"/app/ml-project-2-la_team/website/img/date/",
    "Dot and Date":"/app/ml-project-2-la_team/website/img/dotdate/",
    "Invisible_Dot":"/app/ml-project-2-la_team/website/img/invisible_dot/",
    "logo":"/app/ml-project-2-la_team/website/img/logo.png",
    "logo_cropped":"/app/ml-project-2-la_team/website/img/logo_cropped.png"
}
textAfterMetrics = {
    "Raw":"""""",
    "Dot":"""""",
    "Date":"""""",
    "Dot and Date":"""""",
    "Invisible_Dot":""""""
}

def getImage(name,num=-1):
    try:
        if num != -1 :
            return Image.open(path[name] + str(num) + ".jpeg")
        return Image.open(path[name])
    except:
        if num != -1 :
            return Image.open(pathDeploy[name] + str(num) + ".jpeg")
        return Image.open(pathDeploy[name])