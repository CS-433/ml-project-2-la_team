import streamlit as st
from helper_website import hide_streamlit

# ---- SIDEBAR ----
st.sidebar.header("Please Choose Here a dataset and metrics to see if they will give you meaningful results:")

filters = {
    "metrics":["Grad Cam","Auroc","Odd Ratio","Risk Ratio","Likelihood Positive","Likelihood Negative","Positive predictive value","Negative predictive value","Confidence Interval","Standard deviation","p values",]
}

metrics = st.sidebar.multiselect(
    "Select the Metrics :",
    options=filters["metrics"],
    default=filters["metrics"][0],
)
# MAIN
st.write("""
You will see in the next chapter why the raw dataset is the one working the best. 
But Computer scientists exists no ? They could remove automatically the red markers, they are so good ^^.
        
There is a major flow, we cannot create information which means that we can just remove a dot by replacing it by the mean color of its neighbours pixels.

Check this image, it is really difficult to make the difference """)

st.image("../data/demo_images/invisible_dot.png")


st.write("Now let's compute use this dataset and check what it returns : ")

st.write("#TODO run pipeline") #TODO

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

st.write("As you can see removing dot changes absolutely nothing, the model stay biaised !") #TODO

st.write("Go to the label leakage for more information !")


st.markdown(hide_streamlit(), unsafe_allow_html=True)
