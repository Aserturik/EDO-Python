import numpy as np


def f1(x, y):
    return x**2 - 10*x + y**2 + 8


def f2(x, y):
    return x*y**2 + x - 10*y + 8


def g1(x, y):
    return (1/10)*(x**2 + y**2 + 8)


def g2(x, y):
    return (1/10)*(x*y**2 + x + 8)


x0, y0 = 0, 0
k = 0
d = 10
eps1 = 1e-6
max_iter = 20
X0 = np.array([x0, y0], dtype=float)
x1 = g1(x0, y0)
y1 = g2(x1, y0)
X1 = np.array([x1, y1], dtype=float)
d = np.linalg.norm(X1 - X0)
while d > eps1 and k < max_iter:
    print(f'| {k:^9} | {x0:^12.6f} | {y0:^12.6f} | {d:^12.6f} |')
    if k == 0:
        print('| Iteración |     x0      |     y0      |     d      |')
    x0, y0 = x1, y1
    k += 1
    X0 = np.array([x0, y0], dtype=float)
    x1 = g1(x0, y0)
    y1 = g2(x1, y0)
    X1 = np.array([x1, y1], dtype=float)
    d = np.linalg.norm(X1 - X0)

if d <= eps1:
    print('Convergencia alcanzada.')
    print(f'Raíz aproximada: x = {x1:.6f}, y = {y1:.6f}')
else:
    print('No se alcanzó la convergencia en el número máximo de iteraciones.')
    print(f'Última aproximación: x = {x1:.6f}, y = {y1:.6f}')
