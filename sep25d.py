# 1. Basic Filtering + Sum
# Given an array of marks:
#marks = np.array([45, 78, 23, 90, 67, 88, 34, 59])
# → Filter only marks greater than 50
# → Find the sum of these filtered marks

import numpy as np

marks = np.array([45,78,23,90,67,88,34,59])
a =marks[(marks>50)]
print(a)
print(np.sum(a))
