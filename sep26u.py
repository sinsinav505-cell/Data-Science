#  unique() – Find unique elements in an array
# =======================================
# Q9: Given: arr = np.array([2, 4, 4, 2, 5, 5, 7, 7, 7])
# → Find all the unique values and how many times each occurs

import numpy as np
arr = np.array([2, 4, 4, 2, 5, 5, 7, 7, 7])
b, c = np.unique(arr, return_counts=True)  #b- unique values  c- for count
print(b)
print(c)

