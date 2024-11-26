
import numpy as np
import cv2

blackimg = np.zeros([100,600,1],'uint8')
cv2.imshow("Black",blackimg)
print("BLACK IMG :",blackimg[0,0,:])

greyImg = np.ones([200,200,3],'uint8')
greyImg *= (127)
cv2.imshow("Grey",greyImg)
print(greyImg[0,0,:])

# Here pixel has more has wider spectrum  
whiteImg = np.ones([400,200,4],'uint16')
whiteImg *= (2**16 -1)
cv2.imshow("White",whiteImg)
print(whiteImg[0,0,:])



colorImg = greyImg.copy()
#BGR Fomrat
colorImg[:,:] = (27,27,2**7)
cv2.imshow("color",colorImg)
print("Color at the pixel",colorImg[0,0,:])



cv2.waitKey(0)
cv2.destroyAllWindows()