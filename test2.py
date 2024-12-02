import pytesseract
from pytesseract import Output
import cv2

img = cv2.imread("tessPy/np13.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #grayscaled
val,img = cv2.threshold(img,100,255,cv2.THRESH_OTSU,1)  #otsu thresh applied
img = 255-img   #inverted
cv2.imshow("IMG",img)


text = pytesseract.image_to_string(image=img)
print(text if len(text)!= 0 else "cant scan")

cv2.waitKey(0)
cv2.destroyAllWindows()