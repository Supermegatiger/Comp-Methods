import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    x = np.zeros(n, dtype=float)

    for i in range(n):
        max_row = i
        max_val = abs(A[i][i])

        # Find the row with the maximum value in the current column
        for j in range(i + 1, n):
            if abs(A[j][i]) > max_val:
                max_val = abs(A[j][i])
                max_row = j

        # Swap rows to bring the max element to the pivot position
        A[[i, max_row]] = A[[max_row, i]]
        b[i], b[max_row] = b[max_row], b[i]

        # Elimination step
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            b[j] -= factor * b[i]
            A[j, i:] -= factor * A[i, i:]

    # Backward substitution
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i][i]

    return x

# Пример использования:
A = np.array([[1e-4,1],[1,2]], dtype=float)
b = np.array([1,4], dtype=float)

x = gauss_elimination(A, b)
print("Решение системы уравнений:")
print(x)