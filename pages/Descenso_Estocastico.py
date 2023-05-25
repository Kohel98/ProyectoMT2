import streamlit as st
import pandas as pd
import numpy as np

tab1, tab2, tab3 = st.tabs(["Definiciones","Ejemplos","Aplicaciones"])
with tab1:
    st.tittle(":blue[**Descenso del gradiente estocastico**]")
    """
    La palabra ' estocástico ' significa un sistema o proceso vinculado con una probabilidad aleatoria. Por lo tanto, en Stochastic Gradient Descent, se
    seleccionan aleatoriamente algunas muestras en lugar de todo el conjunto de datos para cada iteración. En Gradient Descent, hay un término llamado "lote"
    que denota el número total de muestras de un conjunto de datos que se utiliza para calcular el gradiente para cada iteración. En la optimización típica de Gradient Descent, como Batch Gradient Descent, el lote se toma como el
    conjunto de datos completo. Aunque usar todo el conjunto de datos es realmente útil para llegar a los mínimos de una manera menos ruidosa y menos aleatoria, el problema surge cuando nuestro conjunto de datos crece. 
    
     En SGD, utiliza solo una sola muestra, es decir, un tamaño de lote de uno, para realizar cada iteración. 
     La muestra se mezcla aleatoriamente y se selecciona para realizar la iteración.
     
     Stochastic Gradient Descent (SGD) es una variante del algoritmo Gradient Descent que se utiliza 
     para optimizar los modelos de aprendizaje automático. En esta variante, solo se usa un ejemplo de entrenamiento aleatorio para }
     calcular el gradiente y actualizar los parámetros en cada iteración.
     
     Desventajas:
      + :blue[Actualizaciones ruidosas:] Las actualizaciones en SGD son ruidosas y tienen una varianza alta,
      lo que puede hacer que el proceso de optimización sea menos estable y generar oscilaciones alrededor del mínimo.
      
      + :blue[Convergencia lenta:] SGD puede requerir más iteraciones para converger al mínimo, 
      ya que actualiza los parámetros para cada ejemplo de entrenamiento uno a la vez.
      
      + :blue[Convergencia lenta:] SGD puede requerir más iteraciones para converger al mínimo, 
      ya que actualiza los parámetros para cada ejemplo de entrenamiento uno a la vez.
      
      + :blue[Menos preciso:] debido a las actualizaciones ruidosas, SGD puede no converger al mínimo global exacto y puede resultar en una solución subóptima.
      Esto se puede mitigar mediante el uso de técnicas como la programación de la tasa de aprendizaje y las actualizaciones basadas en el impulso.
    
    """
    