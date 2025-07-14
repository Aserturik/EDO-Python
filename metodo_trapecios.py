# Método de los trapecios# Este código implementa el método de los trapecios para aproximar la integral definida de una función.
import numpy as np


a, b, n = -1, 1, 6


def f(x):
    return np.exp(-x**2)


h = (b-a)/(n-1)

x = np.linspace(a, b, n)

print("x:", x)

integral = f(x[0]) + f(x[n-1])
for i in range(1, n - 1):
    integral += 2 * f(x[i])

integral *= h / 2
print("Integral:", integral)
