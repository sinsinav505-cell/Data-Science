# reshape() – Change the shape of an array

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(3, 2)   # 2 rows, 3 columns
print(reshaped)
