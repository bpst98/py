# Basic tesseract test

import numpy as np
import pytesseract
import cv2

img = cv2.imread("tessPy/np.jpg") 
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("IMAGE",img)
text = pytesseract.image_to_string(image=img)
print(text if len(text)!= 0 else "cant scan")

cv2.waitKey(0)
cv2.destroyAllWindows()