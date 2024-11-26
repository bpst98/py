# OSD orientation detection

from PIL import Image
import pytesseract
import matplotlib.pyplot as plt

img = Image.open("tessPy/np6.png")
# img = Image.open("tessPy/np5.jpg")
plt.imshow(img)


text = pytesseract.image_to_string(image=img)
print(text if len(text)!= 0 else "cant scan")
try:
    info = pytesseract.image_to_osd(image=img)
    print(info)
except Exception as e:
    print("EXCEPTION: ",e)
finally:
    plt.waitforbuttonpress(timeout=-1)
