#pathfinder clearing using HSV and dilation/erosion

import numpy as np
import cv2
import matplotlib.pyplot as plt

img  = cv2.imread("warehouse.jpg")

# cv2.imshow("original Img :", img)
hsvImage = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)

h = hsvImage[:,:,0]
s = hsvImage[:,:,1]
v = hsvImage[:,:,2]

h1,s1,v1 = cv2.split(hsvImage)

lower = np.array([10,50,50])
upper = np.array([90,255,255])

mask = cv2.inRange(hsvImage,lowerb=lower,upperb=upper)


cv2.imshow("MASK :", mask)
cv2.imshow("HSV FORMAT :", hsvImage)


cv2.waitKey(0)
cv2.destroyAllWindows()
