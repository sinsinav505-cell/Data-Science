# 2. Given the 2D array:
# arr = np.array([[1, 2, 3, 4],
#                 [5, 6, 7, 8],
#                 [9, 10, 11, 12]])
# → Slice out the subarray containing [[6, 7], [10, 11]].

import numpy as np
a=np.array([[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12]])
print(a[1:3,1:3])