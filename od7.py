#fill the image(with noise) with color
import numpy as np
import cv2
from random import randint
import heapq

img = cv2.imread("fuzzy.png",1)
cv2.imshow("Original", img)
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gauss = cv2.GaussianBlur(grayImg,(3,3),0)

adaptImg = cv2.adaptiveThreshold(gauss,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,205,1)

contours,hierarchy = cv2.findContours(adaptImg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print(len(contours))
contoursAreaList = [ cv2.contourArea(c) for c in contours]
maxvals = heapq.nlargest(5,contoursAreaList)

print(maxvals)

maxValsList = []

for c in contours : 
    if cv2.contourArea(c)>maxvals[3] :
        maxValsList.append(c)

# print(c)

blank = np.zeros([img.shape[0],img.shape[1],3],'uint8')

for c in maxValsList:

    cv2.drawContours(image=blank,
                    contours=[c],
                    contourIdx=-1,
                    color=(randint(10,255),randint(0,255),randint(0,255)),
                    thickness=-8,
                    lineType=1
                    )

cv2.imshow("IMAGE ANS",blank)

cv2.waitKey(0)
cv2.destroyAllWindows()