import streamlit as st
from helper_website import *
import time

st.set_page_config(page_icon=":computer:")

st.title("Step 4: Fixing the dataset.")
st.sidebar.image(getImage("logo_cropped"))
st.markdown(
    """Your clever insistence has revealed a major flaw in the company’s model and they quickly remove the dot from the TB+ cases. """
)
st.image(getImage("Invisible_Dot", 1))
st.markdown("""It is now carefully filled and invisible to your inspection""")

if st.button("Run the model again !"):

    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 2)

    st.markdown(
        """
    Woah the accuracy has been maintained! 
    """
    )

st.markdown("What a great model!... or is it?")

if st.button("Run GradCAM !"):

    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 2)

    st.markdown(
        """

    INSERT image with same gradcam as before
    
    Nope…same results!
    > TIP: even if you can’t see it, the model can. Small nuances in resolution invisible to the naked eye can bias the model.
    """
    )

st.markdown("""---""")
st.markdown("""Now we give the company data sets in which no dot has ever been added""")
st.image(getImage("Date", 1))

if st.button("Run the model !"):
    m = Metrics("Date")
    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 2)

    st.markdown(
        """Woah the accuracy has been mostly maintained! Now """ + m.accuracy() + "%"
    )

st.markdown("What a great model!... or is it?")

if st.button("Run GradCAM again !"):

    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 2)

    st.markdown(
        """

    What?! Now it is using the date?! 

    Ah yes…indeed there was a TB epidemic and the date would reveal the TB
    """
    )

st.markdown("""---""")
st.markdown("Ok…so now we provide them with totally raw images.")


if st.button("Run raw model !"):
    m2 = Metrics("Raw")
    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 2)

    st.markdown(
        """
    Ok """
        + m2.accuracy()
        + """% accuracy…that is similar to a human and quite reasonable given that there are many cases the the GeneXpert does not pick up too.
    """
    )


if st.button("Run GradCAM one last time !"):

    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 2)

    st.markdown(
        """

    Show good gradcam image
    Great! I would use these areas to make my interpretation too!

    """
    )

st.markdown(hide_streamlit(), unsafe_allow_html=True)
