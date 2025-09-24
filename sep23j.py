
# 10. Write a program to generate two (2, 3) and (3, 2) random integer matrices.
#     - Compute A @ B (valid matrix multiplication).
#     - Try B @ A (check the result shape).
# → Compare the two outputs

import numpy as np
a=np.array([[1,2,3],
            [4,5,6]])

b=np.array([[1,2],
            [4,5],
            [7,8]])

c=a@b
v=b@a

print(c)
print(c.shape)

print(v)
print(v.shape)

#a@b is 2 by 2 shape and b@a is 3 by 3 shape . 
# The order of multiplying rows and column changes in both.so they have different results.