from PIL import Image, ImageFilter
from PIL.ImageFilter import (
     BLUR, CONTOUR, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
     EMBOSS, FIND_EDGES, SHARPEN
)

def sharpenPic(curImg, counter):
     current = Image.open(curImg)
     newImg = current.filter(SHARPEN)
     newImg.save('image' + str(counter) + '.jpg')

def blurPic(curImg, counter):
     current = Image.open(curImg)
     newImg = current.filter(BLUR)
     newImg.save('image' + str(counter) + '.jpg')

def rotateCounter(curImg, counter):
     newImg = Image.open(curImg)
     newImg.rotate(90).save('image' + str(counter) + '.jpg')
     
def rotateClock(curImg, counter):
     newImg = Image.open(curImg)
     newImg.rotate(270).save('image' + str(counter) + '.jpg')
    
def cropPic(curImg, counter):
     current = Image.open(curImg)
     width, height = current.size
     left = width / 4
     top = height / 4
     right = 3 * width / 4
     bottom = 3 * height / 4
     newImg = current.crop((left, top, right, bottom))
     newImg.save('image' + str(counter) + '.jpg')
     
def sketchPic(curImg, counter):
     current = Image.open(curImg)
     newImg = current.filter(CONTOUR)
     newImg.save('image' + str(counter) + '.jpg')
     
def oilPic(curImg, counter):
     current = Image.open(curImg)
     newImg = current.filter(EDGE_ENHANCE)
     newImg.save('image' + str(counter) + '.jpg')
     
def pencilPic(curImg, counter):
     current = Image.open(curImg)
     newImg = current.filter(EDGE_ENHANCE_MORE)
     newImg.save('image' + str(counter) + '.jpg')
     
def foilPic(curImg, counter):
     current = Image.open(curImg)
     newImg = current.filter(EMBOSS)
     newImg.save('image' + str(counter) + '.jpg')
     
def negativePic(curImg, counter):
     current = Image.open(curImg)
     newImg = current.filter(FIND_EDGES)
     newImg.save('image' + str(counter) + '.jpg')
