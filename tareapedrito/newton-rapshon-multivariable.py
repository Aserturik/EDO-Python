import numpy as np


def f1(x, y):
    return x**2 - 10*x + y**2 + 8


def f2(x, y):
    return x*y**2 + x - 10*y + 8


def f1x(x, y):
    # Derivada pracial de f1 respecto a x
    h = 1e-6
    return (f1(x + h, y) - f1(x-h, y)) / (2*h)


def f1y(x, y):
    # Derivada pracial de f1 respecto a y
    h = 1e-6
    return (f1(x, y + h) - f1(x, y-h)) / (2*h)


def f2x(x, y):
    # Derivada pracial de f2 respecto a x
    h = 1e-6
    return (f2(x + h, y) - f2(x-h, y)) / (2*h)


def f2y(x, y):
    # Derivada pracial de f2 respecto a y
    h = 1e-6
    return (f2(x, y + h) - f2(x, y-h)) / (2*h)


x0, y0, k, eps, d, maxiter = 0, 0, 0, 0.0001, 10, 100

# Vector X0
X0 = np.array([x0, y0], dtype=float)


# Matriz Jacobiana
J = np.array([[f1x(x0, y0), f1y(x0, y0)],
              [f2x(x0, y0), f2y(x0, y0)]], dtype=float)


# vector F
F = np.array([-f1(x0, y0), -f2(x0, y0)], dtype=float)


# Vector H
H = np.linalg.solve(J, F)

x1 = X0[0] + H[0]
y1 = X0[1] + H[1]

X1 = np.array([x1, y1], dtype=float)

d = np.linalg.norm(X1 - X0)

while d > eps and k < maxiter:
    print(f'|k: {k:^9} | x0: {x0:^12.6f} | y0: {y0:^12.6f} | d: {d:^12.6f} |')
    x0, y0, k = x1, y1, k + 1
    X0 = np.array([x0, y0], dtype=float)
    J = np.array([[f1x(x0, y0), f1y(x0, y0)],
                  [f2x(x0, y0), f2y(x0, y0)]], dtype=float)
    F = np.array([-f1(x0, y0), -f2(x0, y0)], dtype=float)
    H = np.linalg.solve(J, F)
    x1 = X0[0] + H[0]  # revisar el h con 2 componentes
    y1 = X0[1] + H[1]
    X1 = np.array([x1, y1], dtype=float)
    d = np.linalg.norm(X1 - X0)
if d <= eps:
    print('Convergencia alcanzada.')
    print(f'Raíz aproximada: x = {x1:.6f}, y = {y1:.6f}')
else:
    print('No se alcanzó la convergencia en el número máximo de iteraciones.')
    print(f'Última aproximación: x = {x1:.6f}, y = {y1:.6f}')
