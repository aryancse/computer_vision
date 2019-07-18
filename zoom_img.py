#!/usr/bin/python3

#importing required modules
import cv2 as cv

img=cv.imread('large.jpg') # reading the image 
cv.imshow('image',img) # the actual image

scalex=0.9  # defining the measure of x-axis
scaley=0.9 #defining the measure of y-axis

#resize function called 
scaleup=cv.resize(img,None,fx=scalex*3,fy=scaley*3,interpolation=cv.INTER_LINEAR)
cv.imshow('zoom',scaleup) # the zoom image
cv.waitKey(0) # window is open untill we press any key
cv.destroyAllWindows()



