#!/usr/bin/python3
#importing some modules
import cv2 as cv
import numpy as np
img=cv.imread('wp3778678.jpg')
#split into BGR
x,y,z=cv.split(img)
myimg=np.zeros((512,512))
 
#to draw line,rectangle ,circle
cv.line(img,(0,0),(150,160),(255,0,0),3)
cv.rectangle(img,(50,50),(100,110),(255,0,0),2)
cv.imshow('my',img)

#now to wait for the window
cv.waitKey(0)

