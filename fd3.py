#EYE DETECTION : works only on brightness ! not color value
import numpy as np
import cv2

img = cv2.imread("faces.jpeg")
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cascadeClassifier = cv2.CascadeClassifier("haarcascade_eye.xml")

eyes = cascadeClassifier.detectMultiScale(grayImg,scaleFactor=1.02,minNeighbors=20,minSize=(10,10))

print(len(eyes))

for (x,y,w,h) in eyes :
    cx = int((x + x + w)/2)
    cy = int((y + y + h)/2)
    r = int(w/2)
    cv2.circle(img=img,center=(cx,cy),radius= r,color=(0,255,0),thickness= 2)

cv2.imshow("Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()