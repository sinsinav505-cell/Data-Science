# 2. Filtering + Mean
# Given an array:
#arr = np.array([12, 45, 67, 89, 34, 22, 90, 100])
# → Select values between 40 and 90 (exclusive)
# → Calculate their mean

import numpy as np

arr = np.array([12, 45, 67, 89, 34, 22, 90, 100])
b=arr[(arr>40)&(arr<90)]
print(b)
print(np.mean(b))