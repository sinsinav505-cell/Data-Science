# 7. Verify the shape of the result when multiplying a (4, 3) matrix with a (3, 2) matrix.

import numpy as np
a=np.array([[1,2,3],
          [4,5,6],
          [7,8,9],
          [4,7,3]])
b=np.array([[2,3],
           [1,5],
           [7,8]])
c=a@b
print(c)
print(c.shape)