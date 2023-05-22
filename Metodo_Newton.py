
import streamlit as st
import pandas as pd
import numpy as np
add_selectbox = st.sidebar.selectbox(
         " ",("Metodo de Newton", "Metodo de Cuasi-Newton")
)


with st.sidebar:
         st.radio(
                  "elige",
                  ("1","2")
         )
