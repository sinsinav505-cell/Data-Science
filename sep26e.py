#vstack() and hstack() – Stack vertically or horizontally

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

vertical = np.vstack((a, b))
horizontal = np.hstack((a, b))

print(vertical) # Row-wise
print(horizontal) #column-wise
