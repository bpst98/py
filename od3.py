#skin detection

import numpy as np
import cv2

img = cv2.imread('faces.jpeg',1)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

hsv_split =  np.concatenate((h,s,v),axis=1)
cv2.imshow("HSVsplit", hsv_split)


ret,minSat = cv2.threshold(s,40,255,cv2.THRESH_BINARY)
cv2.imshow("SAT MIN", minSat)
ret, maxHue = cv2.threshold(h,15,255,cv2.THRESH_BINARY_INV)
cv2.imshow("HUE MAX", maxHue) 


combinedIMG = cv2.bitwise_and(minSat,maxHue)
cv2.imshow("combined Filter: ",combinedIMG)

cv2.waitKey(0)
cv2.destroyAllWindows()