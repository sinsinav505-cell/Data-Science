# 10. Filter with Logical NOT (~)
# Given:
#arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
# → Filter all elements NOT greater than 40
# → Compute the mean of these remaining elements

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
b = arr[~(arr>40)]
print(b)
c = arr[(arr>40)]
print(c)
print(np.mean(c))