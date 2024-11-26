# Morph Erosion & Dilation
import cv2
import numpy as np

img = cv2.imread("emoji.png",1)
cv2.imshow("Original Image",img)



#median blur
blurImg = cv2.medianBlur(img,11)
cv2.imshow("Blurred Median",blurImg)


#gaussian blur
blurImg2 = cv2.GaussianBlur(img, (11,11),0)
cv2.imshow("Gauss Blur",blurImg2)


kernel = np.ones((5,5),'uint8')

#dilation = brighten up
dilateImg = cv2.dilate(img,kernel,iterations=1)
cv2.imshow("dilated Image ",dilateImg)

#erosion = brighten up
erodeImg = cv2.erode(img,kernel,iterations=1)
cv2.imshow("eroded Image ",erodeImg)


# ========OPEN /CLOSE morph ops =======================================

openImg = cv2.morphologyEx(img,cv2.MORPH_OPEN,(3,3))
cv2.imshow("Open Image ",openImg)




cv2.waitKey(0)
cv2.destroyAllWindows()