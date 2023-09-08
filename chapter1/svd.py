import numpy as np

matrix = np.array([[1,2],[3,4]])

another_matrix = np.dot(matrix,matrix.T)

print(another_matrix)

U,s,V = np.linalg.svd(another_matrix)

print(U)
print(s)
print(V)