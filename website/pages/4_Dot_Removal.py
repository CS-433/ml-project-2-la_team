import streamlit as st
from helper_website import *

st.set_page_config(page_icon=":computer:")
# ---- SIDEBAR ----
st.sidebar.header(
    "Please Choose Here metrics to see if the dataset will give meaningful results:"
)

metrics = sidebarMetrics()
# MAIN
st.title("Remove the dot !")
st.write(
    """
You will see in the next chapter why the raw dataset is the one working the best. 
But Computer scientists exists no ? They could remove the red markers automatically for you, they are so good ^^.
        
Let's ask your friend to remove this unnecessary information on your pictures so you can train your model again on a freshly cleaned dataset.
 """
)

c1, c2, c3 = st.columns([1, 1, 1])
with c1:
    st.image(getImage("Invisible_Dot", 1))
with c2:
    st.image(getImage("Invisible_Dot", 2))
with c3:
    st.image(getImage("Invisible_Dot", 3))

st.write("""It seems they did a really good job ! Look at it you cannot even see the dot on this pictures anymore.

Let’s get back to business.""")

st.write("Now let's use this dataset and check what it returns : ")

metricsFunction(metrics)

st.write("""Results are more or less the same how could that be ? 

You see, your “professional” friend wasn’t so pro after all and mistakenly did not erased the red dot correctly. It’s not visible with the naked eye but that computer absolutely picked up that difference in color by 0.40% on the bottom right corner of your images of ill patients.

As you cannot create information out of nothing he just replaced the red dot by the mean color below it.
""")

st.write(textAfterMetrics["Invisible_Dot"])

st.write("Go to the label leakage for more information !")


st.markdown(hide_streamlit(), unsafe_allow_html=True)
