# 7. Chained Conditions + Aggregation
'''Create a random array of 15 integers between 1 and 100'''
# → Filter numbers either less than 20 OR greater than 80
# → Find their mean and sum

import numpy as np

a=np.random.randint(1,101,size=15)
b=a[(a<20)|(a>80)]
print(b)
print(np.mean(b))
print(np.sum(b))