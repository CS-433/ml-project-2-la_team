# ML Project 2 : Create an Interactive Teaching Tool for Medical Doctors to Understand how Machine Learning Models Work (and how they Break!)

# Website URL

https://bias-ml-slayer.streamlit.app/

# Setup

Website (local) : 
- Install requirements from requirements.txt.
- Go to website foler
- run this command : "streamlit run Main.py"

NoteBook : 
#TODO @ColinPelletier

# Repository content

```
|
\
src
  | model_tools.py       Tools to define the architecture of the model
  | pipeline_tools.py    Tools to import image for the pipeline
  | poison_images.py     Script used to resize and poison images with dot/date/invisible_dot
  | predToBinary.py      Script used to get Binary predition (0 or 1) from range prediction file ([0..1])
\
results     # contains some of our results from the data exploration

\
notebooks
  | data_exploration.ipynb : analyze the distribution of the dataset images according to the width/height ratio
  | gradcam.ipynb : run Grad-CAM on a pre-trained model and output the Grad-CAM image
  | ml_pipeline.ipynb : import dataset, train, test model and export predictions
 \
data        # raw data used to compute metrics in the site

\
generated   # generated data from notebooks

\
res         # resources 

\
website
  \
  img       # images used in the website

  \
  pages     # Pages of the website sequentially followed by user

  | helper_website.py   Tools used to avoid redundancy between the website pages
  | Main.py             File used to launch the site, main page
  | metrics.py          Computation and display of metrics in the website
  | path_constants.py   Dictionnaries of constants to get path of the resource needed by the site
  | style.css           Style sheet

```
## Authors :

- Joris Monnet
- Colin Pelletier
- Killian Raude

