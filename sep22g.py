# 7. Verify the shape of the result when multiplying a (3, 2) matrix with a (2, 4) matrix.

import numpy as np
A=np.array([[1,2],
            [3,4],
            [5,6]])
B=np.array([[1,2,3,4],
            [5,6,7,8]])
c=A@B
print(c)
print(c.shape)
