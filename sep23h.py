# 8. Given:
# A = np.array([[3, 1], [0, 2]])
# B = np.array([[4], [5]])
# → Perform matrix multiplication (A @ B) and explain the result.

import numpy as np
A = np.array([[3, 1], 
              [0, 2]])

B = np.array([[4],
              [5]])
print(A@B)

#A is 2 by 2 matrix and B is 2 by 1 matrix. So after multiplying the rows and columns, 
# the result will be a 2 by 1 matrix.