# 5. Multiply a matrix by a column vector
# Given:
#A = np.array([[2, 4],[6, 8],[10, 12]])
#c = np.array([[1],[2],[3]])
# → Multiply A by c elementwise using broadcasting.


import numpy as np
A = np.array([[2, 4],
              [6, 8],
              [10, 12]])
c = np.array([[1],
              [2],
              [3]])

b=A*c
print(b)