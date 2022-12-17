import streamlit as st
from PIL import Image

import numpy as np
from multiprocessing import Process, Queue

# from autooed.problem import build_problem, get_problem_config
# from autooed.utils.initialization import get_initial_samples

# Containers
header = st.container()

st.header('This app displays the result of the DGEMO algorithm. ')

st.subheader('  Gaussian process surrogate model was build on \
just 57 empirical data points and through efficient sampling in the \
design space; algorithm was able to obtain \
Pareto optimal solution in just 6 iterations. This \
greatly reduces number of experiments thus saving time and resources. \
The candidate process parameters prescribed by model, \
were experimentally validated and tested.')

# Select
# root_folder = st.sidebar.text_input('Upload data',value='demo_files/')

if st.button('Run experiment'):
    hv = Image.open('figures/hyper57.png')

    st.image(hv, caption='Figure 1. Performance results. (a) The scatter plot of hardness \
        versus porosity (Pareto front is colored red) open magenta marks represents \
        candidate configuration and solid magenta marks denotes suggested \
        configuration after evaluation. (b) Hypervolume improvement plot on the \
        right represents advancements toward Pareto front.',width =500)    

    design_space = Image.open('figures/performance57.png')

    st.image(design_space, caption='Figure 2. The scatter plot of a) \
        porosity [%] and b) hardness [HV] as a function of VED.',width =650)    


st.markdown('If you are interested in making stand-alone app for industrial\
    applications, please contact me Timur.Chepiga@skoltech.ru')


