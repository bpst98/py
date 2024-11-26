#contour IMG

import cv2
import numpy as np

img = cv2.imread("blob.png",1)

cv2.imshow("org",img)


grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# cv2.imshow("GRAY",grayImg)


threshImg = cv2.adaptiveThreshold(grayImg,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

cv2.imshow("THRESH IMG",threshImg)


contoursThresh, hierarchy = cv2.findContours(threshImg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# NOTE: mode   cv2.RETR_TREE: ----------------------------- Retrieves all contours and reconstructs a full hierarchy of nested contours.
# NOTE: method cv2.CHAIN_APPROX_SIMPLE: ------------------- removes all redundant points and compresses the contour, thereby saving memory.

newImg = img.copy()

thickness = 2
index = -1
randcolor = (234,4,132)

cv2.drawContours(newImg,contoursThresh,index,randcolor,thickness,cv2.LINE_4)
print(contoursThresh)

cv2.imshow("NEW IMAGE",newImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
