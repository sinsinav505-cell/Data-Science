# 8. Scale each column differently
# Given:
#A = np.array([[1, 2, 3],[4, 5, 6]])
#scale = np.array([2, 3, 4])
# → Multiply A by scale so each column is scaled differently.

import numpy as np
A = np.array([[1, 2, 3],[4, 5, 6]])
scale = np.array([2, 3, 4])
c=A*scale
print(c)