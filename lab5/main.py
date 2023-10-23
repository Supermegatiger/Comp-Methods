import numpy as np
import matplotlib.pyplot as plt

n = 0
x_0 = []
eps = 1e-6


def jacobi(A,b):
    # начальные приближения
    x0 = x_0

    x = x0.copy()
    k = 0
    res = []
    while not k or any(abs(x - x0) >= eps):
        x0 = x.copy()
        k+=1
        for i in range(n):
            x[i] = (b[i]-np.dot(A[i,:i],x0[:i]) - np.dot(A[i,i+1:],x0[i+1:]))/A[i][i]
        res.append(max(b-np.dot(A,x)))

    print('\nМетод Якоби')
    print(f'Решение:\n{x}')
    print(f'Кол-во итераций: {k}')
    plt.plot(list(range(k)),res)
    plt.annotate(f'{res[-1]:.7}',
                 xy=(k-1, res[-1]),
                 xytext=(k-1 - 1.2, res[-1] + 0.2),
                 arrowprops={'arrowstyle': '->'})
    
def seidel(A,b):
    # начальные приближения
    x0 = x_0

    x = x0.copy()
    k = 0
    res = []
    while not k or any(abs(x - x0) >= eps):
        x0 = x.copy()
        k+=1
        for i in range(n):
            x[i] = (b[i]-np.dot(A[i,:i],x[:i]) - np.dot(A[i,i+1:],x0[i+1:]))/A[i][i]
        res.append(max(b-np.dot(A,x)))
    
    print('\nМетод Зейделя')
    print(f'Решение:\n{x}')
    print(f'Кол-во итераций: {k}')
    plt.plot(list(range(k)),res)
    plt.annotate(f'{res[-1]:.7}',
                 xy=(k-1, res[-1]),
                 xytext=(k-1 - 1.2, res[-1] + 0.2),
                 arrowprops={'arrowstyle': '->'})




A = np.array([[12.14, 1.32, -0.78, -2.75],
              [-0.89, 16.75, 1.88, -1.55],
              [2.65, -1.27, -15.64, -0.64],
              [2.44, 1.52, 1.93, -11.43]],dtype=float)

b = np.array([14.78, -12.14, -11.65, 4.26],dtype=float)

n = len(b)
# начальные приближения
x_0 = np.zeros(n,dtype=float) # нули
# x_0 = np.random.rand(n) # рандомные числа
print(f'Начальные приближения:\n{x_0}')
jacobi(A,b)
seidel(A,b)
plt.legend(['Метод Якоби', 'Метод Зейделя'])
plt.show()
