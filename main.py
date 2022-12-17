import streamlit as st
from PIL import Image

import numpy as np
from multiprocessing import Process, Queue

# from autooed.problem import build_problem, get_problem_config
# from autooed.utils.initialization import get_initial_samples

# Containers
header = st.container()

st.header('This app displays the result of the DGEMO algorithm. ')

# Select
# root_folder = st.sidebar.text_input('Upload data',value='demo_files/')


    

if st.button('Run experiment'):
    hv = Image.open('figures/hyper57.png')

    st.image(hv, caption='hypervolume',use_column_width ='auto')    

    design_space = Image.open('figures/performance57.png')

    st.image(design_space, caption='design space',use_column_width ='auto')    



