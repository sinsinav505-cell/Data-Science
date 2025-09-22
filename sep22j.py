# 10. Write a program to generate two (3, 3) matrices with random integers and compute:
#     - A @ B (matrix multiplication)
#     - A * B (element-wise multiplication)
# → Compare the outputs.

import numpy as np
A=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
B=np.array([[2,3,4],
            [4,5,6],
            [7,8,1]])
print(A@B)
print(A*B)

#A@B performs matrix multiplication using rows*column concept.
#A*B performs element wise multiplication by directly multiplying elements from both matrices.