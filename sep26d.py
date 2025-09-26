#split() – Split an array into multiple parts

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
b = np.split(arr, 3)
print(b)