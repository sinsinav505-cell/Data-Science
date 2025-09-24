# 2. Add a row vector to a matrix
# Given:
#A = np.array([[1, 2, 3],[4, 5, 6]])
#b = np.array([10, 20, 30])
# → Use broadcasting to add b to each row of A.

import numpy as np
A=np.array([[1,2,3],[4,5,6]])
B=np.array([10,20,30])
c=A+B
print(c)