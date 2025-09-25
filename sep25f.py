# 3. Filtering + Max
#Create a 2D array of random integers between 10 and 100 with shape (3, 4)
# → Filter all values greater than 50
# → Find the maximum among the filtered values

import numpy as np

a=np.random.randint(10,100, size=(3,4))
print(a)
b=a[(a>50)]
print(b)
print(np.max(b))