import cv2

def boxDraw(data,img,i,thick,color):
    x = data['left'][i]     #X axis start -left
    y = data['top'][i]      #y axis start - top
    w = data['width'][i]
    h = data['height'][i]

    cv2.rectangle(img=img,pt1=(x,y),pt2=(x+w,y+h),color=color,thickness=thick)

    return x,y,w,h