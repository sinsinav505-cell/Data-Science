#concatenate - 2D array

#concatenate() – Join two or more arrays

import numpy as np

a = np.array([[1, 2, 3],[9,7,8]])
b = np.array([[4, 5, 6],[5,4,1]])
c= np.concatenate((a, b),axis=0) #row-wise
d= np.concatenate((a, b),axis=1) #column-wise
print(c)
print(d)