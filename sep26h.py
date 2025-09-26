#ravel() – Similar to flatten(), returns a view (faster)

import numpy as np

arr2D = np.array([[10, 20], [30, 40]])
ravelled = arr2D.ravel()
print(ravelled)