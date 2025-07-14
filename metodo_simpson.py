# Metodo de Simpson
import numpy as np


a, b, n = -1, 1, 3
n = 2*n


def f(x):
    return np.exp(-x**2)


h = (b-a)/(n-1)

x = np.linspace(a, b, n)

print("x:", x)

integral = f(x[0]) + f(x[n-1])
for i in range(1, n - 1):
    if i % 2 == 0:
        integral += 2 * f(x[i])
    else:
        integral += 4 * f(x[i])


integral *= h / 3
print("Integral:", integral)
