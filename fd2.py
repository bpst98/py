#FACE DETECTION : works only on brightness ! not color value
import numpy as np
import cv2

img = cv2.imread("faces.jpeg")

grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cascadeClassifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

face = cascadeClassifier.detectMultiScale(grayImg,scaleFactor= 1.04,minNeighbors = 20,minSize=(100,100))

print(len(face))

print(face)


for (x,y,w,h) in face : 
    cv2.rectangle(img,(x,y),(x+w,y+h),(110,255,0),thickness=2)

cv2.imshow("Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
