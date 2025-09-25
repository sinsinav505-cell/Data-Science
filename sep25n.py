# 11. Create a 5×5 array of random integers between 1 and 100
# → Filter elements that are multiples of 5
# → Find their sum, mean, and total count

import numpy as np

a = np.random.randint(1,101,size=(5,5))
print(a)
b=a[(a%5==0)]
print(b)
print(np.sum(b))
print(np.mean(b))
print(np.size(b))