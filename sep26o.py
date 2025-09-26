#  ravel() – Similar to flatten(), returns a view (faster)
# =======================================
# Q3: Given: arr = np.array([[1, 2, 3], [4, 5, 6]])
# → Use ravel() to convert it into 1D and change the 0th element of the result to 100
# → Check if the original array changes

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
b=arr.ravel()
print(b)
b[0]=100
print(b)
print(arr)
