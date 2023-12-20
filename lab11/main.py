import numpy as np
import matplotlib.pyplot as plt

# Аналитическое решение
ans = lambda x,t : np.exp(-t) * np.sin(x)


L = np.pi / 2
T = 1
Nx = 10
# Этот шаг делает схемы устойчивыми
Nt = 2*Nx**2

# -0.5 для улучшения погрешности ()
dx = L / (Nx-0.5)
dt = T / Nt

# Условие устойчивости Куранта-Фридрихса-Леви (r <= 1/2)
r = dt / (dx ** 2)

x_values = np.linspace(0, L, Nx)
t_values = np.linspace(0, T, Nt)
u = np.zeros((Nx, Nt))
u1 = np.zeros((Nx, Nt))

# Начальные условия
u[:, 0] = np.sin(x_values)
# Граничные условия
u[0, :] = 0
u[-1, :] = np.exp(-t_values)

# Явная разностная схема
for t in range(0, Nt - 1):
    for x in range(1, Nx - 1):
        u[x, t + 1] = r * u[x - 1, t] + (1 - 2 * r) * u[x, t] + r * u[x + 1, t]


# Неявная разностная схема
        
# Нач. условия
u1[:, 0] = np.sin(x_values)
# Гранич. условия
u1[0, :] = 0
u1[-1, :] = np.exp(-t_values)


# Решение неявной разностной схемы с использованием метода прогонки
for t in range(0, Nt-1):
    A = np.eye(Nx-1) * (1 + 2*r)
    A += np.eye(Nx-1, k=-1) * (-r)
    A += np.eye(Nx-1, k=1) * (-r)
    b = u1[1:Nx, t]
    b[0] += r * u1[0, t+1]
    b[-1] += r * u1[-1, t+1]
    u1[1:Nx, t+1] = np.linalg.solve(A, b)


# Построение решения
X, T = np.meshgrid(x_values, t_values)

fig, axs = plt.subplots(1, 3, figsize=(12, 5))

# fig = plt.figure()
axs[0] = fig.add_subplot(131, projection='3d')
axs[0].plot_surface(X, T, u.T, cmap='inferno')
axs[0].set_title('Явная разностная схема')

axs[2] = fig.add_subplot(132, projection='3d')
axs[2].plot_surface(X, T, u1.T, cmap='inferno')
axs[2].set_title('Неявная разностная схема')

axs[1] = fig.add_subplot(133, projection='3d')
axs[1].plot_surface(X, T, ans(X,T), cmap='inferno')


# Средняя погрешность
mn1 = np.mean([np.mean([abs(i-j) for i,j in zip(u.T, ans(X,T))])])
mn2 = np.mean([np.mean([abs(i-j) for i,j in zip(u1.T, ans(X,T))])])
print(f'Средняя ошибка для явного метода: {mn1:.4f}')
print(f'Средняя ошибка для неявного метода: {mn2:.4f}')

plt.show()

