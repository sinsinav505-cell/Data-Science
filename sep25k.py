# 8. Aggregation on Condition
# Given a 2D array:
'''matrix = np.array([[23, 45, 67],
                   [89, 12, 34],
                   [56, 78, 90]])'''
# → Filter all even numbers
# → Calculate their maximum and minimumm

import numpy as np

matrix = np.array([[23, 45, 67],
                   [89, 12, 34],
                   [56, 78, 90]])

a=matrix[(matrix%2==0)]
print(a)
print(np.max(a))
print(np.min(a))