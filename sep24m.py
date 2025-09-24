# 9. Incompatible shapes
# Given:
#a = np.array([1, 2, 3])   # shape (3,)
#b = np.array([1, 2])      # shape (2,)
# → Try adding a + b. What error do you expect? Why?

import numpy as np
a = np.array([1, 2, 3])
b = np.array([1, 2])
c=a+b
print(c)

#could not broadcast , bcz of different shapes.