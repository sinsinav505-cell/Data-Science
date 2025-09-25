# 5. Filter Before Sum
# Create a 2D array:
'''array = np.array([[10, 20, 30],
                  [40, 50, 60],
                   [70, 80, 90]])'''
# → Filter elements greater than 30 and less than 80
# → Compute the sum of these filtered elements

import numpy as np

array = np.array([[10, 20, 30],
                  [40, 50, 60],
                  [70, 80, 90]])
a=array[(array>30)&(array<80)]
print(a)
print(np.sum(a))