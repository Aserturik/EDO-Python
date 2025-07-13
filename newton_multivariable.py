import numpy as np


def f1(x, y, z):
    return y * np.sin(x)+np.cos(x)-z


def f2(x, y, z):
    return np.exp(x+y)-(x**2*np.cos(x)-(np.pi/1.15))


def f3(x, y, z):
    return y+3*x*z+x**3


def f1x(x, y, z):
    h = 0.000001
    return (f1(x + h, y, z) - f1(x - h, y, z)) / (2 * h)


def f1y(x, y, z):
    h = 0.000001
    return (f1(x, y + h, z) - f1(x, y - h, z)) / (2 * h)


def f1z(x, y, z):
    h = 0.000001
    return (f1(x, y, z + h) - f1(x, y, z - h)) / (2 * h)


def f2x(x, y, z):
    h = 0.000001
    return (f2(x + h, y, z) - f2(x - h, y, z)) / (2 * h)


def f2y(x, y, z):
    h = 0.000001
    return (f2(x, y + h, z) - f2(x, y - h, z)) / (2 * h)


def f2z(x, y, z):
    h = 0.000001
    return (f2(x, y, z + h) - f2(x, y, z - h)) / (2 * h)


def f3x(x, y, z):
    h = 0.000001
    return (f3(x + h, y, z) - f3(x - h, y, z)) / (2 * h)


def f3y(x, y, z):
    h = 0.000001
    return (f3(x, y + h, z) - f3(x, y - h, z)) / (2 * h)


def f3z(x, y, z):
    h = 0.000001
    return (f3(x, y, z + h) - f3(x, y, z - h)) / (2 * h)


def jacobiano(x, y, z):
    return np.array([
        [f1x(x, y, z), f1y(x, y, z), f1z(x, y, z)],
        [f2x(x, y, z), f2y(x, y, z), f2z(x, y, z)],
        [f3x(x, y, z), f3y(x, y, z), f3z(x, y, z)]
    ])


def F(x, y, z):
    return np.array([f1(x, y, z), f2(x, y, z), f3(x, y, z)])


# Metodo de Newton multivariable
x0, y0, z0, k, eps, max_iter = 0, 0, 0, 0, 0.0001, 20
X = np.array([x0, y0, z0], dtype=float)
d = 10

print("Iteración | x | y | z | ||F(x,y,z)|| | error")
print("-" * 60)

while d > eps and k < max_iter:
    F_val = F(X[0], X[1], X[2])

    norm_F = np.linalg.norm(F_val)

    print(f'{k:^9} | {X[0]:6.4f} | {X[1]:6.4f} | {
          X[2]:6.4f} | {norm_F:10.6f} | {d:8.6f}')

    J = jacobiano(X[0], X[1], X[2])

    try:
        delta_X = np.linalg.solve(J, -F_val)
    except np.linalg.LinAlgError:
        print("Error: El jacobiano es singular")
        break

    # Actualizar el punto
    X_new = X + delta_X

    # Calcular el error (distancia entre iteraciones)
    d = np.linalg.norm(X_new - X)

    X = X_new
    k += 1

# Verificar convergencia
F_final = F(X[0], X[1], X[2])
norm_F_final = np.linalg.norm(F_final)

print("-" * 60)
if norm_F_final <= eps:
    print(f'La solución es x={X[0]:.4f}, y={X[1]:.4f}, z={X[2]:.4f}')
    print(f'Converge en {k} iteraciones')
    print(f'||F(x,y,z)|| = {norm_F_final:.5f}')
else:
    print(f'No se encontró solución en {max_iter} iteraciones')
    print(f'Última aproximación: x={X[0]:.6f}, y={X[1]:.6f}, z={X[2]:.6f}')
    print(f'||F(x,y,z)|| = {norm_F_final:.5f}')
