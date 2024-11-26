#template matching
import numpy as np
import cv2

template = cv2.imread("template.jpg")
img = cv2.imread("players.jpg")
cv2.imshow("PLYAERS",img)

res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

minVal,maxVal,minLoc,maxLoc = cv2.minMaxLoc(res)

print(maxVal,maxLoc)

cv2.circle(res,maxLoc,radius= 20,color=(15,15,114),thickness=2)

cv2.imshow("RESULT",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
