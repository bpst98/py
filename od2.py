#ADAPTIVE THRESHOLD

import cv2
import numpy as np

img  = cv2.imread("sudoku.png",0)

cv2.imshow("original Image",img)

#NOTE: normal threshold

ret, threshIMG = cv2.threshold(img,50,255,cv2.THRESH_BINARY)

kernel = np.ones((2,2),'uint8')

cv2.imshow("Thresh Image",threshIMG)

#NOTE: Adaptive threshold
adaptImg = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,113,1)

erodeImg = cv2.erode(adaptImg,kernel,iterations=1)
cv2.imshow("eroded Image ",erodeImg)

dilImg = cv2.dilate(adaptImg,kernel=kernel,iterations=1)
cv2.imshow("dilated Image ",dilImg)


cv2.imshow("ADAPTIVE Image",adaptImg)

cv2.waitKey(0)
cv2.destroyAllWindows()