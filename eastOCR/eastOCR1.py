import cv2
from imutils.object_detection import non_max_suppression as nms

imgPath = "tessPy/np12.jpg"
img = cv2.imread("tessPy/np12.jpg")
h,w = 320,320
detector = "frozen_east_text_detection.pb"
min_conf = 0.9  # minimum confidence

original = img.copy()
print(original.shape)

img = cv2.resize(img,(w,h))
print(img.shape[0],img.shape[1])

# cv2.imshow("IMAGE TRANSFORMED",img)

layer = ['feature_fusion/Conv_7/Sigmoid','feature_fusion/concat_3']
nueralNetwork = cv2.dnn.readNet(detector)

blob = cv2.dnn.blobFromImage(img,1.0,(w,h),swapRB=True,crop=False)
print("BLOB DIMENIONS:",blob.shape)

nueralNetwork.setInput(blob=blob)
scores,geometry = nueralNetwork.forward(layer)

print("GEOMETRY DIMESIONS: ",geometry.shape)
print("SCORES DIMESIONS: ",scores.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()

