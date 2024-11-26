#Corner Detection
import numpy as np
import cv2

img = cv2.imread("emoji.png",1)
img = cv2.resize(img,(0,0),fx=0.6,fy=0.6,interpolation=cv2.INTER_LANCZOS4)

grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("FRAME",grayImg)

corners = cv2.goodFeaturesToTrack(image=grayImg,maxCorners=50,qualityLevel=0.01,minDistance=2)
print(corners.size)

for corner in corners:
    x,y =  corner.ravel()
    # print(x,y)
    cv2.circle(img=img,center=(int(x),int(y)),radius=10,color=(115,0,214),thickness=2)
    
cv2.imshow("CORNERs FRAME",img)

cv2.waitKey(0.2)
cv2.destroyAllWindows()
