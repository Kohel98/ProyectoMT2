
import streamlit as st
import pandas as pd
import numpy as np


st.title(":blue[Metodo de Newton(-Raphson)]")

st.header("Teorema")
"""
El metodo de Newton es una alternativa del metodo del punto 
fijo ya que la gran desventaja de este se consiste en obtener ecuaciones $g_i$ que converja 
en el intervalo de solucion y dicha búsqueda puede representar un esfuerzo de cálculo considerable, en lo unico en que se parecen en estos dos metodos es 
la generalización multivariable del método de Newtoon para una sola variable.

Este metodo solo sirve para los sistemas de ecuaciones no lineales, este requiere algunos conceptos previos, los cuales se presentan a continuación.

La derivada, cuando se trabaja con funciones con varias variables, se emplean las derivadas parciales. La generalización de derivada para sistemas de funciones 
de varias variables es la matriz jacobiana.
:red[_Streamlit_]
"""
