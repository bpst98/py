import cv2
import pytesseract
from pytesseract import Output

img = cv2.imread("tessPy/np12.jpg")
cv2.imshow("CUP IMAGE",img)


imgInfo = pytesseract.image_to_data(image=img,output_type=Output.DICT)
print("IMAGE DATA :",imgInfo['text'])

cv2.waitKey(0)
cv2.destroyAllWindows()

