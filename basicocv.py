#!/usr/bin/python3
#importing the modules
import cv2 as cv

#checking the version
print(cv.__version__)

#images read
img=cv.imread('wp3778678.jpg',-1)
img1=cv.imread('wp3778678.jpg',0)
#  1 means the same color channel BGR
#  0 means the no color channel only black and white
# -1 means the image tranparency
print(img)

#print shape
print(img.shape)

#to display img
cv.imshow('murat',img[0:250,0:150]) #to crop the image 
cv.imshow('m2',img1) # the second window
#to make the window open
cv.waitKey(0)  #0 means for the infinte time or it is in mili/micro sec


