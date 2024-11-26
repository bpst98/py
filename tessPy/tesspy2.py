#detecting text image and bounded it within a rect

import numpy as np
import matplotlib.pyplot as plt
import pytesseract
from PIL import Image
import cv2
from pytesseract import Output

img = cv2.imread("tessPy/np5.jpg")
rgb = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgData = pytesseract.image_to_data(img,output_type=Output.DICT)

def boxDraw(data,img,i,color = (34,45,233)):
    x = data['left'][i]     #X axis start -left
    y = data['top'][i]      #y axis start - top
    w = data['width'][i]
    h = data['height'][i]

    cv2.rectangle(img=img,pt1=(x,y),pt2=(x+w,y+h),color=color)

    return x,y,w,h

call = imgData['text']

for i in range(0,len(call)):
    confidence = imgData['conf'][i]     #confidence value

    if not call[i].isalnum():
        continue
    x,y,w,h = boxDraw(imgData,img,i)
    print(f"x: {x} y: {y} w: {w} h: {h}")
    # print("confidence :",confidence," WORD:",call[i])

cv2.imshow("IMAGE:",img)

cv2.waitKey(0)
cv2.destroyAllWindows()