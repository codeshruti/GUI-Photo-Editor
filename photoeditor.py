import streamlit as st
import numpy as np
import cv2
from  PIL import Image, ImageEnhance, ImageFilter
import streamlit as st
st.set_page_config(page_title='Photo Editor')
st.title("Photo Editor Application")

def grayscale(img):
	gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
	st.image(gray_scale, width=300)
	#return gray_scale

def blackwhite(img):
	gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
	slider = st.sidebar.slider('Adjust the intensity', 1, 255, 127, step=1)
	(thresh, blackAndWhiteImage) = cv2.threshold(gray_scale, slider, 255, cv2.THRESH_BINARY)
	st.image(blackAndWhiteImage, width=300)
	#return blackAndWhiteImage
	
def sketch(img):
	gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
	inv_gray = 255 - gray_scale
	slider = st.sidebar.slider('Adjust the intensity', 25, 255, 125, step=2)
	blur_image = cv2.GaussianBlur(inv_gray, (slider,slider), 0, 0)
	sketch = cv2.divide(gray_scale, 255 - blur_image, scale=256)
	st.image(sketch, width=300) 
	#return sketch
	
def blurimg(img):
	slider = st.sidebar.slider('Adjust the intensity', 5, 81, 33, step=2)
	converted_img = cv2.cvtColor(converted_img, cv2.COLOR_RGB2BGR)
	blur_image = cv2.GaussianBlur(converted_img, (slider,slider), 0, 0)
	st.image(blur_image, channels='BGR', width=300)

def sharpimg(img):
	converted_img = cv2.cvtColor(converted_img, cv2.COLOR_RGB2BGR)
	kernel = np.array([[0, -1, 0],[-1, 5,-1],[0, -1, 0]])
	image_sharp = cv2.filter2D(src=converted_img, ddepth=-1, kernel=kernel)
	st.image(image_sharp, width=300)
	
#def imgcall():
st.title("Upload an image")
uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'])

#return image,uploaded_file	
from PIL.ImageFilter import (
     BLUR, CONTOUR, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
     EMBOSS, FIND_EDGES, SHARPEN
)

st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
st.sidebar.title('Edit Options')
bt1 = st.sidebar.button('Gray Image')
bt2 = st.sidebar.button('Black and White')
bt3 = st.sidebar.button('Pencil Sketch')
bt4 = st.sidebar.button('Blur Effect')
bt5 = st.sidebar.button('Sharpen')
#converted_img,uploaded_file = imgcall()
if uploaded_file is not None:
	converted_ = Image.open(uploaded_file)
	converted_img = np.array(converted_.convert('RGB'))
	st.markdown('Photo',unsafe_allow_html=True)
	if bt1:
		grayscale(converted_img)
	elif bt2:
		#blackwhite(converted_img)
		converted_img = np.array(converted_img.convert('RGB'))
		gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
		slider = st.sidebar.slider('Adjust the intensity', 1, 255, 127, step=1)
		(thresh, blackAndWhiteImage) = cv2.threshold(gray_scale, slider, 255, cv2.THRESH_BINARY)
		st.image(blackAndWhiteImage, width=300)
	elif bt3:
		sketch(converted_img)
	elif bt4:
		blurimg(converted_img)
	elif bt5:
		sharpimg(converted_img)	
	else: 
		st.image(converted_img, width=300)
