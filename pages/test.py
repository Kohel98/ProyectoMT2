import streamlit as st
from PIL import Image



image = Image.open('Image.jpg')

st.image(image, caption='Sunrise by the mountains')