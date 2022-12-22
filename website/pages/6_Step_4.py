import streamlit as st
from helper_website import *
import time

PROGRESS_BAR_TIMING = 0.01

getPage("Step 4: Fixing the dataset.", False, True)

st.markdown(
    """Your clever insistence has revealed a major flaw in the company’s model and they quickly remove the dot from the pneumonia positive cases. """
)

displayImages("Invisible_Dot")
st.markdown("""It is now carefully filled and invisible to your inspection""")

if st.button("Run the model again !"):
    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(PROGRESS_BAR_TIMING)
        my_bar.progress(percent_complete + 1)

    st.markdown("""Woah the accuracy has been maintained!""")

st.markdown("What a great model!... or is it?")

if st.button("Run GradCAM !"):

    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(PROGRESS_BAR_TIMING)
        my_bar.progress(percent_complete + 1)

    # st.image(getGradcam("Invisible_dot")) TODO
    st.markdown(
        """Nope…same results!
    > TIP: even if you can’t see it, the model can. Small nuances in resolution invisible to the naked eye can bias the model.
    """
    )

st.markdown("""---""")
st.markdown("""Now we give the company data sets in which no dot has ever been added""")
displayImages("Date")

if st.button("Run the model !"):
    m = Metrics("Date")
    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(PROGRESS_BAR_TIMING)
        my_bar.progress(percent_complete + 1)

    st.markdown(
        """Woah the accuracy has been mostly maintained! Now """
        + str(m.accuracy())
        + "%"
    )

st.markdown("What a great model!... or is it?")

if st.button("Run GradCAM again !"):
    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(PROGRESS_BAR_TIMING)
        my_bar.progress(percent_complete + 1)

    st.image(getGradcam("Date"))
    st.markdown(
        """
    What?! Now it is using the date?! 

    Ah yes…indeed there was a pneumonia epidemic and the date would reveal the pneumonia
    """
    )

st.markdown("""---""")
st.markdown("Ok…so now we provide them with totally raw images.")

displayImages("Raw")
if st.button("Run raw model !"):
    m2 = Metrics("Raw")
    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(PROGRESS_BAR_TIMING)
        my_bar.progress(percent_complete + 1)

    st.markdown(
        """
    Ok """
        + str(m2.accuracy())
        + """% accuracy…that is similar to a human and quite reasonable given that there are many cases the the GeneXpert does not pick up too.
    """
    )


if st.button("Run GradCAM one last time !"):
    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(PROGRESS_BAR_TIMING)
        my_bar.progress(percent_complete + 1)

    st.image(getGradcam("Date_original"))  # TODO
    st.markdown(
        """Show good gradcam image
    Great! I would use these areas to make my interpretation too!

    """
    )