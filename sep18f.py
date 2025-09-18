import numpy as np
a= [[1, 2, 3, 5, 9, 8],
    [4, 5, 6, 7, 8, 9]]
arr = np.array(a)

print(arr[1,0:4]) 
print(arr[0:2,1]) 
print(arr[0:2,1:4])