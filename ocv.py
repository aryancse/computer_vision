#!/usr/bin/python3

import cv2 as cv

#checking the version
print(cv.__version__)

#image reading
img=cv.imread('wp3778678.jpg')
print(img)


#print shape 
print(img.shape)

#to display the img
cv.imshow('murat',img)
