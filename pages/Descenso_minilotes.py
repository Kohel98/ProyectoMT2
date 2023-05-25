import streamlit as st
import pandas as pd
import numpy as np

tab1, tab2, tab3 = st.tabs(["Definiciones","Ejemplos","Aplicaciones"])
with tab1:
    st.tittle(":red[** Descenso de gradiente de mini lotes **]")
    """
        En el aprendizaje automático, el descenso de gradiente es una técnica de optimización 
        utilizada para calcular los parámetros del modelo (coeficientes y sesgo) para algoritmos 
        como la regresión lineal, la regresión logística, las redes neuronales, etc. 
        
        En esta técnica, iteramos repetidamente a través del conjunto de 
        entrenamiento y actualizamos el modelo. parámetros de acuerdo con el 
        gradiente del error con respecto al conjunto de entrenamiento. 
        
        :red[Descenso de gradiente de minilote:] los parámetros se actualizan después de calcular 
        el gradiente del error con respecto a un subconjunto del conjunto de entrenamiento.
        
        Dado que se considera un subconjunto de ejemplos de entrenamiento, 
        puede realizar actualizaciones rápidas en los parámetros del modelo 
        y también puede aprovechar la velocidad asociada con la vectorización del código.
        
        Según el tamaño del lote, las actualizaciones se pueden hacer menos ruidosas: cuanto mayor 
        sea el tamaño del lote, menos ruidosa será la actualización.
    """