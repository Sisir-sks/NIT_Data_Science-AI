import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
from PIL import Image
from io import BytesIO
st.set_page_config(page_title='Image Classification',layout='wide')
@st.cache_data

def load_image(url):
    response=requests.get(url)
    return Image.open(BytesIO(response.content))

st.title('Image-Multi channel visualiser')
image_url=st.text_input('Enter URL here',value=(r'https://images.unsplash.com/photo-1575936123452-b67c3203c357?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D'))

loaded_image=load_image(image_url)

#display
st.image(loaded_image, caption=' Original Image',use_container_width=True)

image_np=np.array(loaded_image)

R,G,B=image_np[:,:,0],image_np[:,:,1],image_np[:,:,2]

# creating channel images
red_img=np.zeros_like(image_np)
red_img[:,:,0]=R

green_img=np.zeros_like(image_np)
green_img[:,:,1]=G

blue_img=np.zeros_like(image_np)
blue_img[:,:,2]=B

# Display RGB channels
st.subheader("RGB Channel Visualization")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(red_img, caption="Red Channel", use_container_width=True)

with col2:
    st.image(green_img, caption="Green Channel", use_container_width=True)

with col3:
    st.image(blue_img, caption="Blue Channel", use_container_width=True)

# Grayscale + Colormap
st.subheader("Colormapped Grayscale Image")

colormap = st.selectbox(
    "Choose a Matplotlib colormap",
    ["viridis", "plasma", "inferno", "magma", "cividis", "hot", "cool", "gray"]
)

loaded_gray = loaded_image.convert("L")
loaded_gray_np = np.array(loaded_gray)

# Plot using matplotlib with colormap
fig, ax = plt.subplots(figsize=(6, 4))
im = ax.imshow(loaded_gray_np, cmap=colormap)
plt.axis("off")
plt.title(colormap)
st.pyplot(fig)