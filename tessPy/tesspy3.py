# using regular exp for searching methods

import pytesseract
from pytesseract import Output
import cv2
import boxDraw
import re

img = cv2.imread("tessPy/np11.png")
rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

imgInfo = pytesseract.image_to_data(image=rgb,output_type=Output.DICT)

# print(imgInfo)

# NOTE: reg exp for date validation
date_pattern= r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
usd_pattern = "^\$\d{1,3}(,\d{3})*(\.\d{2})?$"


max=int(len(imgInfo['text']))
for i in range(0,max):

    text=imgInfo['text'][i]

    if imgInfo['conf'][i] >30:

        if re.match(date_pattern,text):
            x,y,w,h = boxDraw.boxDraw(imgInfo,img,i,thick=-1,color=(230,10,230))
            print(text)
            cv2.putText(img=img,text=text,org=(x,y-2),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(11,10,230)) #puts a box for date detected
            continue

        x,y,w,h = boxDraw.boxDraw(imgInfo,img,i,2,(0,230,22))
        cv2.putText(img=img,text=text,org=(x,y-2),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(230,50,30)) #overhead text for recognised characters/words
  
cv2.imshow("FRAME",img) 

cv2.waitKey(0)
cv2.destroyAllWindows()