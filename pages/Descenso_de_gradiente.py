import streamlit as st
import pandas as pd
import numpy as np
tab1, tab2, tab3 = st.tabs(["Definiciones","Ejemplos","Aplicaciones"])
with tab1:
         st.title(":blue[Descenso de la Gradiente]")
         """
         Gradient Descent es conocido como uno de los algoritmos de optimización más utilizados
         para entrenar modelos de aprendizaje automático mediante la minimización de errores 
         entre los resultados reales y esperados.
         
         Además, el descenso de gradiente también se usa para entrenar redes neuronales.
         
         El :red[**objetivo principal**] del descenso de gradiente es minimizar la función convexa 
         mediante la iteración de actualizaciones de parámetros. 
         
         Una vez que se optimizan estos modelos de aprendizaje automático,
         estos modelos se pueden usar como herramientas poderosas para la inteligencia artificial 
         y varias aplicaciones informáticas.
         
         Este se define como uno de los algoritmos de optimización iterativos de aprendizaje automático 
         más utilizados para entrenar los modelos de aprendizaje automático y aprendizaje profundo.
         Ayuda a encontrar el mínimo local de una función.
         La mejor manera de definir el mínimo local o el máximo local de una función mediante el descenso de gradiente es la siguiente:
            + Si nos movemos hacia un gradiente negativo o nos alejamos del gradiente de la función 
            en el punto actual, dará el :red[**mínimo local de esa función**].
         """