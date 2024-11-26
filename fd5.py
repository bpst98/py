# Image capture
import cv2
import numpy as np
import math
import time

capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)

capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,700)  
# fps = capture.get(cv2.cv.CV_CAP_PROP_FPS)


cv2.namedWindow("webcam")

if not capture.isOpened() :
    print("error : webcam could not be opened ")
    exit()

while(True) : 
    
    start = time.time()
    ret,frame = capture.read()
    
    flipFrame = cv2.flip(frame,1)
    end = time.time()
    try:
        fps = math.ceil(1/(end - start))    
    except :
        fps = 0
        print("ZERO DIVISION")

    # cv2.putText(frame,"FPS: %(fps) ",(100,100),1,15,(0,144,111),thickness=1)
    
    cv2.putText(flipFrame, str(fps), (7, 70), cv2.FONT_HERSHEY_PLAIN, 3, (100, 255, 0), 3, cv2.LINE_AA) 
    if ret :    
        cv2.imshow("webcam",flipFrame)
    print(fps)


    ch = cv2.waitKey(1)

    if ch & 0xFF == ord('c') :
        # Click photo
        cv2.imwrite(f"pics/CAPTURE{start}.jpg",frame)
        # break

    if ch & 0xFF == ord('q') :
        break



    # print(frame.shape[0],frame.shape[1])


capture.release()
cv2.destroyAllWindows()    
