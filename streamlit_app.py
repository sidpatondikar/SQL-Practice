# -*- coding: utf-8 -*-

import math
import streamlit as st
import pandas as pd
import joblib

# Set the page title
st.set_page_config(
    page_title="SQL Practice Notes",
    page_icon="✅",  # Optionally, you can set an icon for the page
    layout="wide",  # Use "wide" layout for full-width content
)

# Set the background color to black and text color to white
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Customize the heading with green color
st.title('SQL Practice Notes')
st.markdown(
    """
    <style>
    h1 {
        color: green;
    }
    </style>
    """,
    unsafe_allow_html=True,
)