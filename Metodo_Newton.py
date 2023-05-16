
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


:red[**Definición**]. Matriz jacobiana: 

Sean $f_i (x_1, x_2, ..., x_n)$ con $ 1 \leq i \leq n $, funciones con n variables $(x_i)$ independientes. La matriz jacobiana $J(x_1, x_2,..., x_n)$
está dada por las derivadas parciales de cada una de las funciones con respecto a cada una de las variables: 


"""
"J="st.latex(r"""
         \begin{bmatrix} 
         \dfrac{\partial f_1}{\partial x_1} (x_0, x_1, ..., x_n) & b \\ 
         c & d 
         \end{bmatrix}
         """)
