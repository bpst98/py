#  COLOR DETECTION MASK

import cv2
import numpy as np

def setval(x):
    print("Val changed: ",x)

pal = "COLOR PALETTE"
cv2.namedWindow(pal)

#tracker Setup
cv2.createTrackbar("UPPER HUE", pal,150,255,setval)
cv2.createTrackbar("UPPER SAT", pal,255,255,setval)
cv2.createTrackbar("UPPER VAL", pal,255,255,setval)
cv2.createTrackbar("LOWER HUE", pal,64,190,setval)
cv2.createTrackbar("LOWER SAT", pal,72,255,setval)
cv2.createTrackbar("LOWER VAL", pal,49,255,setval)

capture = cv2.VideoCapture(0)

if not capture.isOpened() :
    print("error : webcam could not be opened ")
    exit()

while(True) : 
    
    ret,frame = capture.read()
    #converted to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) 

    #get values from tracker made
    UH = cv2.getTrackbarPos("UPPER HUE",pal)
    LH = cv2.getTrackbarPos("LOWER HUE",pal)

    LS = cv2.getTrackbarPos("LOWER SAT",pal)
    US = cv2.getTrackbarPos("UPPER SAT",pal)
    
    LV = cv2.getTrackbarPos("LOWER VAL",pal)
    UV = cv2.getTrackbarPos("UPPER VAL",pal)

    uHSV = np.array([UH,US,UV])   #defined rangein colorspace #upperbound
    lHSV = np.array([LH,LS,LV])                               #lowerbound

    mask = cv2.inRange(hsv,lHSV,uHSV)   #threshold setup for color range
    
    #bitWise operation

    newframe = cv2.bitwise_and(frame,frame,mask=mask)
    newframe = cv2.medianBlur(newframe,7)


    
    cv2.imshow("WEBCAM",newframe)
    



    ch = cv2.waitKey(1)

    if ch & 0xFF == ord('q') :
        break





cv2.waitKey(0)
cv2.destroyAllWindows()