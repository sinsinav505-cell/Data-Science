#numpy aggregate function

import numpy as np

a=np.array([[1,2,3,4,5],
            [5,6,7,8,9]])

print("Sumof all elements:",np.sum(a)) #sum of all elements 

print(np.mean(a)) #mean value

print(np.max(a)) #maximum element

print(np.min(a)) #minimum element

print(np.argmin(a)) #index of minimum element

print(np.argmax(a)) #index of maximum element

print("Row wise sum",np.sum(a,axis=1)) #add elements in the same row

print("Column wise sum",np.sum(a,axis=0)) #add elements in the same column of each row

print("Product of all elements",np.prod(a)) #product of all elements

print(a.size) #count of array

b = np.random.randint(1,101,size=15)
print(b)
