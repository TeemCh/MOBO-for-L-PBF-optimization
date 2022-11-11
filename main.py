import streamlit as st

# Containers
header = st.container()

st.sidebar.title('Bayesian metal printing')

# Select
root_folder = st.sidebar.text_input('Upload data',value='demo_files/')

with header:
    st.header('Bayesian methods')


