# 9. Create a (4, 4) identity matrix using NumPy and multiply it with a (4, 4) random integer matrix.
# → What do you observe?

# Identity matrix , I = [[1 0 0 0]
#                        [0 1 0 0]
#                        [0 0 1 0]
#                        [0 0 0 1]]


import numpy as np
A=np.eye(4)
B=np.array([[1,2,3,4],
            [2,3,4,5],
            [3,4,5,6],
            [5,6,7,8]])

print(A@B)

#the result is same as the random integer matrix.