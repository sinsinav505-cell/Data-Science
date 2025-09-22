# 9. Create a (3, 3) identity matrix using NumPy and multiply it with a (3, 3) random integer matrix.
# → What do you observe?

#Identity matrix , I = [[1 0 0]
#                       [0 1 0]
#                       [0 0 1]]

import numpy as np
I=np.eye(3)
a=np.array([[1,2,3],
           [4,5,6],
           [7,8,9]])
print(I@a)

#the output is a itself