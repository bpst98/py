#simple threshold

import numpy as np
import cv2

img = cv2.imread("wojak.jpg",0)
h,w = img.shape

cv2.imshow("BW image",img)


binaryIMG = np.zeros([h,w,1],'uint8')
threshold = 65

for row in range(0,h) :
    for col in range(0,w) : 
        if img[row][col] > threshold : 
            binaryIMG[row][col] = 255

# slow binary
cv2.imshow("Binary image",binaryIMG)            

#threshold 
ret, threshold_image = cv2.threshold(img,threshold,255,cv2.THRESH_BINARY_INV)

cv2.imshow("Threshold Image",threshold_image)


cv2.waitKey(0)
cv2.destroyAllWindows