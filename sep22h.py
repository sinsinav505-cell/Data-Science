# 8. Given:
# A = np.array([[2, 0], [1, 3]])
# B = np.array([[1], [4]])
# → Perform matrix multiplication (A @ B) and explain the result.

import numpy as np
A = np.array([[2, 0],
             [1, 3]])
B = np.array([[1],
              [4]])
print(A@B)

#step1 : 
# 2*1 + 0*4 = 2
# 1*1 + 3*4 = 13
