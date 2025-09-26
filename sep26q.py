# concatenate() – Join two or more arrays
# =======================================
# Q5: Given: a = np.array([10, 20, 30]), b = np.array([40, 50, 60])
# → Concatenate these two arrays into one 1D array
# → Also try concatenating them column-wise as a 2D array

import numpy as np

a = np.array([10,20,30])
b = np.array([40,50,60])
c=np.concatenate((a,b))
print(c)

a1=np.array([[10,20,30],
             [40,50,60]])

b1=np.array([[20,40,60],
             [50,30,80]])
c1=np.concatenate((a1,b1))
print(c1)