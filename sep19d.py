#matrix multiplication
import  numpy as np
A=np.array([[1,2],
            [3,4]])
B=np.array([[5,6],
            [7,8]])

print(A@B)

#other methods
print(A.dot(B)) 

print(np.matmul(A,B))