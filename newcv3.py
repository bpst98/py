#Pixel manipulation and filtering

import numpy as np
import cv2

img = cv2.imread("emoji.png",1)

greyImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("GrayImage.png",greyImg)

greyImg2 = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imwrite("GrayImage2.png",greyImg2)

height,width,channel = img.shape


b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

grey_split = np.empty([height*2,width,4],'uint8')

#added transparency layer

grey_split[0:height,:] = cv2.merge((b,g,r,r))
grey_split[height:height*2,:] = cv2.merge((b,g,r,b))


# cv2.imshow("GREY SPLIT",grey_split)
# cv2.imshow("original IMAGE",img)
cv2.imwrite("GreySplittest.PNG",grey_split)
print(img.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()