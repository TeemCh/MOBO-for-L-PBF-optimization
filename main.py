import streamlit as st
from PIL import Image

import numpy as np
from multiprocessing import Process, Queue

# from autooed.problem import build_problem, get_problem_config
# from autooed.utils.initialization import get_initial_samples

# Containers
header = st.container()

st.markdown('Streamlit is **_really_ cool**.')

# Select
# root_folder = st.sidebar.text_input('Upload data',value='demo_files/')

with header:
    st.header('Bayesian methods')

if st.button('Run experiment'):
    st.write('Why hello there')
else:
    st.write('Goodbye')


hv = Image.open('figures/hyper57.png')

st.image(hv, caption='hypervolume',use_column_width ='auto')    

design_space = Image.open('figures/performance57.png')

st.image(design_space, caption='design space',use_column_width ='auto')    



