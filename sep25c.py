#Numpy filtering with Logical operations

#AND , OR, NOT...  &, | , ~ ...

import numpy as np

a = np.array([[50,60,70,30,20],
            [32,99,89,65,21]])

b = a[(a>40)&(a<90)] #and
print("Marks greater than 40 and less than 90 are:",b)

c = a[(a>40)|(a<90)] #or
print("Marks greater than 40 or less than 90 are:",c)

d = a[~(a>40)] #not
print("Marks not greater than 40 are:",d) 

print(a[~(a==20)])




