#  Mixed Challenge
# =======================================
# Q10: Given: arr = np.array([[1, 2, 2], [3, 4, 4], [5, 6, 6]])
# → Flatten it
# → Find the unique values
# → Reshape it into a (2, -1) shape
# → Transpose the reshaped result

import  numpy as np

arr = np.array([[1, 2, 2], [3, 4, 4], [5, 6, 6]])
b=arr.flatten()
print(b)
c=np.unique(b)
print(c)
d=c.reshape(2,-1)
print(d)
print(d.transpose())