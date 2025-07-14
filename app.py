import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

sidepage = st.sidebar.selectbox("Explore or Predict", ("Predict", "Explore")) # it will create selectbox from streamlit app and allow us with options to select

if sidepage == "Predict":
    show_predict_page()
else:
    show_explore_page()