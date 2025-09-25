
# 9. Filter Outside Range
# Given an array:
#arr = np.array([12, 45, 60, 75, 30, 95, 100, 20])
# → Filter all values outside the range 40–90 (<40 or >90)
# → Find the sum and count of these filtered elements

import numpy as np

a= np.array([12, 45, 60, 75, 30, 95, 100, 20])
b = a[(a<40)|(a>90)]
print(b)
print(np.size(b))
print(np.sum(b))