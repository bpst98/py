#simple video capture

import cv2
import numpy as np

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Error: Could not open webcam.")
    exit()

while(True) : 
    
    ret, frame = capture.read()
    flipFrame = cv2.flip(frame,1)

    frame = cv2.resize(frame,(200,200),fx=0.9,fy=2.9)
    cv2.imshow("Capture Frame",flipFrame)
    # cv2.imshow("Capture Frame",frame)

    ch = cv2.waitKey(1) 
    if ch & 0xFF == ord('q') :
        break

capture.release()
cv2.destroyAllWindows()