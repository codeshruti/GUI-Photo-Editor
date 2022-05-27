import streamlit as st
import numpy as np
import cv2
from  PIL import Image, ImageEnhance
import streamlit as st
st.set_page_config(page_title='Photo Editor Application')
st.title("Photo Editor")
st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
st.markdown('<p class="font">Upload your photo here...</p>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'])
if uploaded_file is not None:
	image = Image.open(uploaded_file)
	filter = st.sidebar.radio('Edit Options:', ['Original','Gray Image','Black and White', 'Pencil Sketch', 'Blur Effect'])
	if filter == 'Original':
		st.markdown('<p style="text-align: center;">Original Image</p>',unsafe_allow_html=True)
	else:
		st.markdown('<p style="text-align: center;">Before</p>',unsafe_allow_html=True)
		st.image(image,width=300)  
		st.markdown('<p style="text-align: center;">After</p>',unsafe_allow_html=True)
	if filter == 'Gray Image':
		converted_img = np.array(image.convert('RGB'))
		gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
		st.image(gray_scale, width=300)
	elif filter == 'Black and White':
		converted_img = np.array(image.convert('RGB'))
		gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
		slider = st.sidebar.slider('Adjust the intensity', 1, 255, 127, step=1)
		(thresh, blackAndWhiteImage) = cv2.threshold(gray_scale, slider, 255, cv2.THRESH_BINARY)
		st.image(blackAndWhiteImage, width=300)
	elif filter == 'Pencil Sketch':
		converted_img = np.array(image.convert('RGB')) 
		gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
		inv_gray = 255 - gray_scale
		slider = st.sidebar.slider('Adjust the intensity', 25, 255, 125, step=2)
		blur_image = cv2.GaussianBlur(inv_gray, (slider,slider), 0, 0)
		sketch = cv2.divide(gray_scale, 255 - blur_image, scale=256)
		st.image(sketch, width=300) 
	elif filter == 'Blur Effect':
		converted_img = np.array(image.convert('RGB'))
		slider = st.sidebar.slider('Adjust the intensity', 5, 81, 33, step=2)
		converted_img = cv2.cvtColor(converted_img, cv2.COLOR_RGB2BGR)
		blur_image = cv2.GaussianBlur(converted_img, (slider,slider), 0, 0)
		st.image(blur_image, channels='BGR', width=300) 
	else: 
		st.image(image, width=300)

