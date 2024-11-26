#contour IMG
# NOTE: AREA + PERIMETER + CENTROID

import cv2
import numpy as np

img = cv2.imread("blob.png",1)
#created gray img by converting BGR to Gray
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

threshImg = cv2.adaptiveThreshold(grayImg,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

cv2.imshow("THRESH IMG",threshImg)


contoursThresh, hierarchy = cv2.findContours(threshImg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# NOTE: mode   cv2.RETR_TREE: ----------------------------- Retrieves all contours and reconstructs a full hierarchy of nested contours.
# NOTE: method cv2.CHAIN_APPROX_SIMPLE: ------------------- removes all redundant points and compresses the contour, thereby saving memory.

newImg = img.copy()

thickness = 2
index = -1
randcolor = (234,4,132)

h,w,channels = img.shape

cv2.drawContours(newImg,contoursThresh,index,randcolor,thickness,cv2.LINE_4)
# print(contoursThresh)

blankCanvas = np.zeros([h,w,channels],'uint8')

print(h,w,channels)

for c in contoursThresh :
    cv2.drawContours(blankCanvas,[c],index,randcolor,thickness,1)
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c,True)

    centroidMatrix = cv2.moments(c)
    # print(centroidMatrix)
    cy = int(centroidMatrix['m01']/centroidMatrix['m00'])
    cx = int(centroidMatrix['m10']/centroidMatrix['m00'])

    cv2.circle(newImg,(cx,cy),radius=5,color=(0,133,112),thickness=-1,lineType=1)

    # print(f"Area:{area} \n Perimter : {perimeter} \n Centroid : {cx},{cy}")


cv2.imshow("NEW IMAGE",newImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
