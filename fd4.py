# NOTE: FACE DETECTION FOR URL StREAM


import cv2
import numpy as np
import time
import math
# Open the video stream (replace with your video stream URL or file path)
stream_url = "http://192.168.2.228:8080/video"  # for example, an RTSP or HTTP stream URL
cap = cv2.VideoCapture(stream_url)


# Check if the stream is opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream")    
    print("Error details:", cap.get(cv2.CAP_PROP_FPS))
    exit()



while True:
    # Read a frame from the stream
    start = time.time()
    ret, frame = cap.read()
    end = time.time()
    frame = cv2.flip(frame,1)
    fps = math.ceil(1/(end - start))
    cv2.putText(frame,str(fps),(10,30),cv2.FONT_HERSHEY_SIMPLEX,1, (100, 155, 0), 3, cv2.LINE_AA)
    # fps = cv2.CAP_PROP_FPS
    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cascadeClassifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = cascadeClassifier.detectMultiScale(grayFrame,scaleFactor= 1.05,minNeighbors = 3,minSize=(50,50))

    print("NUMBER OF FACES :",len(faces))

    for (x,y,w,h) in faces : 
        cv2.rectangle(frame,(x,y),(x+w,y+h),(110,255,0),thickness=2)



    # If the frame is read correctly, display it
    if ret:
        cv2.imshow('Video Stream', frame)



    else:
        print("Error: Could not read frame")
        break
    
    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
