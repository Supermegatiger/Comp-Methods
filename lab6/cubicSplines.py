import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
from numpy.polynomial.polynomial import Polynomial


a,b=-1,1
f = lambda x: 1/(1+25*x*x)
plt.figure(num='Кубические сплайны')

x = np.linspace(a,b,100)
y = f(x)    
plt.plot(x, y,label='График 1/(1+25*x^2)')

for n in [5,10,15]:
    t = np.linspace(a,b,n)
    y = f(t)
    yint = scipy.interpolate.CubicSpline(t, y)

    plt.plot(t, y, 'o')
    plt.plot(x, yint(x), '-x',label=f'{n}')
plt.legend()
plt.show()





# import numpy as np
# from scipy.interpolate import lagrange
# x = np.array([0, 1, 2])
# y = x**3
# poly = lagrange(x, y)

# from numpy.polynomial.polynomial import Polynomial
# # Polynomial(poly.coef[::-1]).coef
# import matplotlib.pyplot as plt
# x_new = np.arange(0, 2.1, 0.1)
# plt.scatter(x, y, label='data')
# plt.plot(x_new, Polynomial(poly.coef[::-1])(x_new), label='Polynomial')
# plt.plot(x_new, 3*x_new**2 - 2*x_new + 0*x_new, label=r"$3 x^2 - 2 x$", linestyle='-.')
# plt.legend()
# plt.show()