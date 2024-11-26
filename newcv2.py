import numpy as np
import cv2

coloredImg = cv2.imread("emoji.png")
cv2.imshow("image window",coloredImg)
cv2.moveWindow("image window",0,0)

print(coloredImg.shape)
height,width,channels = coloredImg.shape


b,g,r = cv2.split(coloredImg)

rgb_split = np.empty([height,width*3,3],'uint8')


#random RGB channel merge
rgb_split[:,0:width] = cv2.merge([r,g,b])
rgb_split[:,width:width*2] = cv2.merge([r,b,g])
rgb_split[:,width*2:width*3] = cv2.merge([g,b,r])

cv2.imshow("Channels",rgb_split)
cv2.moveWindow("Channels",0,height)


#HueSaturationValue

hsvImage = cv2.cvtColor(coloredImg,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsvImage)
hsv_split = np.concatenate((h,s,v),axis=1)

cv2.imshow("splitHSV",hsv_split)



cv2.waitKey(0)
cv2.destroyAllWindows()