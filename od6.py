#canny edge detection

import cv2
import numpy as np

img = cv2.imread("tomatoes.jpg",1)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

res, threshImg = cv2.threshold(hsv[:,:,0],29,255,cv2.THRESH_BINARY_INV)
# cv2.imshow("tomato",threshImg)

threshImg2 = cv2.adaptiveThreshold(hsv[:,:,0],255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,115,1)
# cv2.imshow("tomatoes",threshImg2)

combinedImg = cv2.bitwise_and(s,v)

edges1 = cv2.Canny(combinedImg,100,125)
cv2.imshow("EDGE DETECTION TEST",edges1)

edges = cv2.Canny(img,100,125)
cv2.imshow("EDGE DETECTION MAIN",edges)

edges_inv = 255-edges

cv2.imshow("EDGE DETECTION MAIN",edges_inv)

kernel = np.ones((2,2),'uint8')

erodeImg = cv2.erode(edges_inv,kernel,iterations=1)
# cv2.imshow("ERODED IMG", erodeImg)

canny_thresh = cv2.bitwise_and(erodeImg,threshImg)
# cv2.imshow("Canny Thresh",canny_thresh)

contours,hierarchy = cv2.findContours(canny_thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

obj = img.copy()

for c in contours:
    cv2.drawContours(img,[c],-1,(0,150,130),1,1)

    M = cv2.moments(c)
    # print(M)
    if M["m00"]!= 0 :     
        cx = int(M['m10']/M['m00'])    
        cy = int(M['m01']/M['m00'])
    # cv2.circle(obj,(cx,cy),4,(124,123,100),-1)




cv2.imshow("IMAGETOM",img)
cv2.waitKey(0)
cv2.destroyAllWindows()