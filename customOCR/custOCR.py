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
digits_label = np.htstack([train_labels,test_labels])


cv2.waitKey(0)
cv2.destroyAllWindows()

