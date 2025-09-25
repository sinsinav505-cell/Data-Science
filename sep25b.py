#numpy filtering - process of selecting elements from an array that match a given condition.

import numpy as np
a=np.array([[50,60,70,80,40],
            [30,99,88,20,90]])

#basic filtering
marks = a[a>40] 
print("All marks>40:",marks)