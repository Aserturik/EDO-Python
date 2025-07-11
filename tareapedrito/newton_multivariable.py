import numpy as np


def f1(x, y):
    return x**2 - 10*x+y**2+8


def f2(x, y):
    return x*y**2+x-10*y+8


def f1x(x, y):
    h = 0.000001
    return (f1(x + h, y) - f1(x-h, y)) / (h * 2)


def f2y(x, y):
    h = 0.000001
    return (f2(x, y + h) - f2(x, y-h)) / (h * 2)


x0, y0, k, d, eps, max_iter = 0, 0, 0, 10, 0.0001, 20
X0 = np.array([x0, y0], dtype=float)
x1 = x0-f1(x0, y0) / f1x(x0, y0)
y1 = y0-f2(x0, y0) / f2y(x0, y0)
X1 = np.array([x1, y1], dtype=float)
d = np.linalg.norm(X1 - X0)

while d > eps and k < max_iter:
    print(f'|k{k:0.0f}| x0={x0:0.4f} | x1={x1:0.4f} | d={d:0.4f}')
    x0, y0, k = x1, y1, k + 1
    X0 = np.array([x0, y0], dtype=float)
    x1 = x0 - f1(x0, y0) / f1x(x0, y0)
    y1 = y0 - f2(x0, y0) / f2y(x0, y0)
    X1 = np.array([x1, y1], dtype=float)
    d = np.linalg.norm(X1 - X0)


if d <= eps:
    print(f'la solucion es x={x1:0.4f}, y={y1:0.4f} en {k} iteraciones')
else:
    print(f'no se encontro solucion en {max_iter} iteraciones')
