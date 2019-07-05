#!/usr/bin/python3
# detecting a face
import cv2 as cv
# calling classifier
casclf=cv.CascadeClassifier('face.xml')
#loading face data 
cap=cv.VideoCapture(0)

while cap.isOpened():
    status,frame=cap.read()
    #now we can apply classifier in live frame 
    face=casclf.detectMultiScale(frame,1.5,5)  # classifier tuning parameter
    #print(face)
    for x,y,h,w in face:
        cv.rectangle(frame,(x,y),(x+h,y+w),(0,0,255),2)
        cv.imshow('face',frame)
        if cv.waitKey(10) & 0xff ==ord('q'):
            break
        

cv.destroyAllWindows()
cap.release()
