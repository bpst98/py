#text detection  using EAST OCR

import cv2
from imutils.object_detection import non_max_suppression as nms
import numpy as np
import pytesseract

imgPath = "tessPy/np12.jpg"
img = cv2.imread("tessPy/np12.jpg")
h,w = 320,320
detector = "frozen_east_text_detection.pb"
min_conf = 0.9  # minimum confidence

original = img.copy()
print(original.shape)

propH = img.shape[0]/h
propW = img.shape[1]/w

img = cv2.resize(img,(w,h))
print(img.shape[0],img.shape[1]," PROPORTIONS: ",propH,propW)
# cv2.imshow("img then",img)

# cv2.imshow("IMAGE TRANSFORMED",img)

layer = ['feature_fusion/Conv_7/Sigmoid','feature_fusion/concat_3']
nueralNetwork = cv2.dnn.readNet(detector)

blob = cv2.dnn.blobFromImage(img,1.0,(w,h),swapRB=True,crop=False)
print("BLOB DIMENIONS:",blob.shape)

nueralNetwork.setInput(blob=blob)
scores,geometry = nueralNetwork.forward(layer)

print("GEOMETRY DIMESIONS: ",geometry.shape)
print("SCORES DIMESIONS: ",scores.shape)

rows, columns = scores.shape[2:4]
print(rows, columns)

boxes = []  #boxes list
conf = []   #confident list

def geometric_data(geometry,y) :

    xData0 = geometry[0,0,y]
    xData1 = geometry[0,1,y]
    xData2 = geometry[0,2,y]
    xData3 = geometry[0,3,y]
    angleData = geometry[0,4,y]
     
    return xData0,xData1,xData2,xData3,angleData

def geometricCalculation(xData0,xData1,xData2,xData3,angleData):

    (offsetX, offsetY) = (x * 4.0, y * 4.0)
    angle = angleData[x]
    cos = np.cos(angle)
    sin = np.sin(angle)
    h = xData0[x] + xData2[x]
    w = xData1[x] + xData3[x]

    endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
    endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))

    beginX = int(endX - w)
    beginY = int(endY - h)

    return beginX, beginY, endX, endY

for y in range(0,rows):
    dataScores = scores[0,0,y]
    xData0,xData1,xData2,xData3,angleData = geometric_data(geometry,y)
    # print(dataScores,"\n =============================================== \n",xData0,xData1,xData2,xData3,angleData)
    for x in range(0,columns):
        if dataScores[x] < min_conf:
            continue
        beginX,beginY,endX,endY = geometricCalculation(xData0,xData1,xData2,xData3,angleData)
        conf.append(dataScores[x])
        boxes.append((beginX,beginY,endX,endY))

print(conf)
print(boxes)

detection = nms(np.array(boxes),probs= conf)
print("DETECTION location: ",detection)

imgCopy = original.copy()
errMargin = 3   # the chances of lose some best information is lower. that is why to increase the bounding region

for(beginX,beginY,endX,endY) in detection:
    beginX = int(beginX*propW)
    beginY = int(beginY*propH)
    endX = int(endX*propW)
    endY = int(endY*propH)



roi = imgCopy[beginY-errMargin:endY+errMargin,beginX-errMargin:endX+errMargin]
text = pytesseract.image_to_string(image=roi)
print("DETECTED TEXT: ",text)

cv2.rectangle(original,(beginX,beginY),(endX,endY),(0,22,255),2)    # bound a rectangle to the region of interest
cv2.imshow("ROI",roi)
cv2.imshow("IMAGE",original)


cv2.waitKey(0)
cv2.destroyAllWindows()

