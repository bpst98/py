import cv2
import numpy as np

capture = cv2.VideoCapture(0)

green = (0,255,0)

line_width = 9
rad = 90

point = (900,200)

def click(event,x,y,flags,param) : 
    global point,pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        print("clicked : ",x,y)
        point = (x,y)


cv2.namedWindow("webCAM")
cv2.setMouseCallback("webCAM",click)

if not capture.isOpened():
    print("Error : webcam could not be opened")
    exit()   

while(True) :
    ret,frame = capture.read()
    flipFrame = cv2.flip(frame,1)

    h,w,channel = flipFrame.shape
    

    enlargeFrame = cv2.resize(flipFrame,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_LANCZOS4)
    cv2.circle(enlargeFrame,point,rad,green,line_width,1)
    cv2.imshow("webCAM", enlargeFrame)



    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q') :
        break

capture.release()
cv2.destroyAllWindows()
