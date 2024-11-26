import numpy as np

arr = np.arange(16).reshape(4,4)
arr1 = arr*4
newArr = arr*arr1

print(newArr)

mat = np.matrix(arr)
mat2 = np.identity(4)

print(mat2)

newMat = mat*mat2
print(newMat)

