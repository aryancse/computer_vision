#!/usr/bin/python3

import cv2 as cv

cap=cv.VideoCapture(0)

while cap.isOpened():
    status,frame=cap.read() # to take an image

    cv.imshow('dd',frame)
    if cv.waitKey(10)  & 0xff == ord('q'):
        break

cv.destroyAllWindows()
cv.release()
    
