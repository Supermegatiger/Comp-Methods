from numpy import linalg
A = [[0.1, 0.2, 0.3],[0.4, 0.5, 0.6],[0.7, 0.8, 0.9]]
b = [0.1,0.3,0.5]
print(linalg.matrix_rank(A))
# print(linalg.solve(A,b))