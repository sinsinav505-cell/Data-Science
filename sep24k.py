
# 7. Subtract two arrays
# Given:
#a = np.array([[1, 2, 3]])
#b = np.array([[10],[20],[30]])
# → Subtract a - b using broadcasting. What is the result shape?

import numpy as np
a = np.array([[1, 2, 3]])
b = np.array([[10],[20],[30]])
c=a-b
print(c)