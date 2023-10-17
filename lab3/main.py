from math import erf,pi
from numpy import linalg
A = [[1, 0.8, 0.64],
     [1, 0.9, 0.81],
     [1, 1.1, 1.21]]

b = [erf(0.8), erf(0.9), erf(1.1)]

# начальное приближение
x0 = [0, 0, 0]
eps = 1e-6


def gauss_seidel(A, b, x0, eps):
    n = len(A)
    x = x0.copy()
    k=0
    temp = []
    while not k or not any(abs(x[i] - x0[i]) >= eps for i in range(n)):
        k += 1
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(i))
            sum2 = sum(A[i][j] * x0[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum1 - sum2) / A[i][i]
        if x == temp:
            break
        else:
            temp = x.copy()
        x0 = x.copy()
    print(f'Кол-во итераций: {k}') 
    return x

solution = gauss_seidel(A, b, x0, eps)
for i, value in enumerate(solution):
    print(f"x{i+1} = {value}")

xtemp = 1.0
for m in range(100,150):
    res = 0
    nf = 1
    for n in range(m):
        nf *= (n if n else 1)
        res += (((-1)**n)*(xtemp**(2*n+1)))/((nf if n else 1) *(2*n+1))
erfTemp = res*2/(pi)**(1/2)


print(sum(solution),erfTemp)

# sol = linalg.solve(A,b)
# print(sum(sol),erf(1.0))


