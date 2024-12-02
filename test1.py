#OTSU threshold
#uses GRAYSCALE image only using class variance b/w BG and FG

import numpy as np
import cv2

img= cv2.imread("tesspy/np7.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("IMG",img)

# val,thresh = cv2.threshold(gray,thresh=95,maxval=255,type=cv2.THRESH_BINARY)
thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,19,5)

# print(val)
cv2.imshow("THRESH",thresh)

val1,threshOTSU = cv2.threshold(gray,thresh=180,maxval=255,type=cv2.THRESH_OTSU )
# val2,threshOTSU2 = cv2.threshold(img,thresh=180,maxval=235,type=cv2.THRESH_OTSU)

print(val1)
# print(val2)
cv2.imshow("OTSU THRESH",threshOTSU)
# cv2.imshow("OTSU THRESH2",threshOTSU2)

adaptiveGauss = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,23,1)


cv2.imshow("adaptiveGauss",adaptiveGauss)

cv2.waitKey(0)
cv2.destroyAllWindows()

