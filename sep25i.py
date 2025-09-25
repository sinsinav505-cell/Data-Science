# 6. Count Filtered Elements
# Given an array of student scores:
#scores = np.array([34, 56, 78, 90, 45, 66, 89, 91, 50])
# → Filter scores above 60
# → Find how many such scores there are (count)
# → Find their average

import numpy as np

scores = np.array([34, 56, 78, 90, 45, 66, 89, 91, 50])
a=scores[(scores>60)]
print(a)
print(np.size(a))
print(np.average(a))