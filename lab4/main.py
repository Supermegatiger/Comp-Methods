import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    x = np.zeros(n, dtype=float)

    for i in range(n):
        max_row = i
        max_val = abs(A[i][i])

        for j in range(i + 1, n):
            if abs(A[j][i]) > max_val:
                max_val = abs(A[j][i])
                max_row = j
        
        A[[i, max_row]] = A[[max_row, i]]
        b[i], b[max_row] = b[max_row], b[i]

        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            b[j] -= factor * b[i]
            A[j, i:] -= factor * A[i, i:]

    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i][i]

    return x

A = np.array([[1e-4,1],[1,2]], dtype=float)
b = np.array([1,4], dtype=float)
ans = [2.0004000800160032007, 0.99979995999199839967]
x = gauss_elimination(A, b)
print("Решение системы уравнений:")
print(x)
print("Неувязка:")
print(b-np.dot(A,x))


A = np.array([
    [2.34, -4.21,-11.61],
    [8.04, 5.22, 0.27],
    [3.92, - 7.99, 8.37]],dtype=float)
b = np.array([ 14.41,-6.44, 55.56],dtype=float)
ans = [2.2930206000048971497, -4.8155221341098955815, 0.9671848741269698301]
x = gauss_elimination(A, b)
print("Решение системы уравнений:")
print(x)
print("Неувязка:")
print(b-np.dot(A,x))

A = np.array([
    [4.43, -7.21,8.05,1.23,-2.56],
    [-1.29, 6.47, 2.96, 3.22, 6.12],
    [6.12, 8.31, 9.41, 1.78, -2.88],
    [-2.57, 6.93, -3.74, 7.41, 5.55],
    [1.46, 3.62, 7.83, 6.25, -2.35]
    ],dtype=float)
b = np.array([2.62, -3.97, -9.12, 8.11, 7.23],dtype=float)
ans = [-0.91523173814156470181,-0.70963013967623410821,-0.39260592997693895842,1.928909378803922768,-0.91639159894024114071]
x = gauss_elimination(A, b)
print("Решение системы уравнений:")
print(x)
print("Неувязка:")
print(b-np.dot(A,x))

