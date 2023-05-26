import streamlit as st
from pages import Img

image = Img.open('Image.png')

st.image(image, caption='Sunrise by the mountains')