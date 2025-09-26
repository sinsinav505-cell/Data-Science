#  vstack() and hstack() – Stack vertically or horizontally
# =======================================
# Q6: Given: a = np.array([1, 2, 3]), b = np.array([4, 5, 6])
# → Stack them vertically (as rows)
# → Stack them horizontally (as one long array)
# → Print both results

import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.vstack((a,b)))
print(np.hstack((a,b)))
