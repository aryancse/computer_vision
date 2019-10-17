#!/usr/bin/python3


#to detect the color(red)

# importing modules required
import cv2 as cv

cap=cv.VideoCapture(0) #default camera starts

#camera stauts
while cap.isOpened():
    status,frame=cap.read()
    #detecting red color
    redimg=cv.inRange(frame,(0,0,0),(90,90,255))

    cv.imshow('liveredcolor',redimg)
    if cv.waitKey(10)   &  0xff == ord('q'):
        break

cv.destroyAllWindows()
cap.release()
