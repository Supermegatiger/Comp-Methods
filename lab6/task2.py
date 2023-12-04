import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
from numpy.polynomial.polynomial import Polynomial

# x = np.array([2,3,4,5,6,7])
# f = np.array([4,-2,2,6,1.5,-3])
# r = []
# for i in range(1,len(x)):
#     r.append(x[i-1])
#     r.append((x[i-1]+x[i])/2)
# x = r + [x[-1]]
# r = []
# for i in range(1,len(f)):
#     r.append(f[i-1])
#     r.append((f[i-1]+f[i])/2)
# f = r + [f[-1]]
# print(x)
# print(f)

x = np.array([2,3,5,7])
f = np.array([4,-2,6,-3])


def g(a):
    tck = scipy.interpolate.splrep(x, f)
    return scipy.interpolate.splev(a, tck)

# print(f(1.25))

a,b=2,7
plt.figure(num='Кубические сплайны')

# x = np.linspace(a,b,100)
y = f    
# plt.plot(x, y,label='График')
plt.plot(x, y, 'o')

# for n in [5]:
    # t = np.linspace(a,b,n)
yint = scipy.interpolate.CubicSpline(x, y, bc_type='clamped')
t = np.linspace(a,b,100)
plt.plot(t, yint(t), '-',label=f'{100}')
plt.legend()
plt.show()

