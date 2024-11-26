import cv2
import numpy as np

img = cv2.imread("wojak.jpg")

#SCALING
imgHalf = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)

cv2.imshow("FULL Image",img)
# cv2.imshow("Halved Image",imgHalf)

h,w,channel = img.shape
print(h,w)

#Rotation
M = cv2.getRotationMatrix2D((h//2,0),45,1)
rotImg = cv2.warpAffine(img,M,(w,h))
print(h,w)
cv2.imshow("RotatedIMAGE",rotImg)

cv2.waitKey(0)
cv2.destroyAllWindows()