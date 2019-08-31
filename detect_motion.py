#!/usr/bin/python3

# to  detect the motion 
import cv2 as cv
#starting the camera
cap=cv.VideoCapture(0)
# if we have a video than at the place of 0 write the video name or url
tp1=cap.read()[1]  #take1
tp2=cap.read()[1]  #take2
tp3=cap.read()[1]  #take3

#  to make more perfect so that do not have any color issue
gray1=cv.cvtColor(tp1,cv.COLOR_BGR2GRAY)   #  converting into grey
gray2=cv.cvtColor(tp2,cv.COLOR_BGR2GRAY)   #  converting into grey
gray3=cv.cvtColor(tp3,cv.COLOR_BGR2GRAY)   #  converting into grey

# now creating image diff
def img_diff(x,y,z):
    #diff b/w   x,y--grey1,grey2 --d1
    d1=cv.absdiff(x,y)
    #diff b/w  y,z --grey2,grey3 --d2
    d2=cv.absdiff(y,z)
    #abs diff d1-d2
    finalimg=cv.bitwise_and(d1,d2)
    return finalimg

#now applying function
while cap.isOpened():
    status,frame=cap.read() #continue image taker
    motionimg=img_diff(gray1,gray2,gray3)
    #  replacing image frame 
    gray1=gray2
    gray2=gray3
    gray3=cv.cvtColor(frame,cv.COLOR_BGR2GRAY) # passing live image to gray3
    cv.imshow('motion',motionimg)
    if cv.waitKey(10) & 0xff == ord('q'):
        break
cv.destroyAllWindows()
cap.release()




