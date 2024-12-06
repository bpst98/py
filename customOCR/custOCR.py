import tensorflow as tf
import numpy as np
import zipfile
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import cv2

from tensorflow.keras.datasets import mnist

(train_data,train_labels), (test_data,test_labels) = mnist.load_data()
print(train_data.shape, test_data.shape)
print(train_labels.shape,test_labels.shape)

digits_data = np.vstack([train_data,test_data])
digits_label = np.hstack([train_labels,test_labels])

digits_data.shape
digits_label.shape


randomIndex = np.random.randint(0,digits_data.shape[0])
plt.imshow(digits_data[randomIndex],cmap='gray')
plt.title('CLASS:'+str(digits_label[randomIndex]))

sns.countplot(x=digits_label[:1000]) 

# cv2.waitKey(0)
# cv2.destroyAllWindows()

