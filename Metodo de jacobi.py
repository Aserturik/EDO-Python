import numpy as np

A = np.array([[4, -1, 0, 0], [-1, 4, -1, 0],
             [0, -1, 4, -1], [0, 0, -1, 4]], dtype=float)
b = np.array([[1], [1], [1], [1]], dtype=float)
B = np.array([[0, 1/4, 0, 0], [1/4, 0, 1/4, 0],
             [0, 1/4, 0, 1/4], [0, 0, 1/4, 0]], dtype=float)
c = np.array([[1/4], [1/4], [1/4], [1/4]], dtype=float)

print('Matriz de coeficientes A:\n', A)
print('(Matriz de terminos independientes) Vector b:\n', b)
print('Matriz de coeficientes B:\n', B)
print('Vector c:\n', c.T)

d, k, eps = 10, 0, 0.0001
X0 = np.array([[0], [0], [0], [0]], dtype=float)
X1 = np.dot(B, X0) + c  # primera iteración
d = np.linalg.norm(X1 - X0)  # ||X1 - x0 ||
print('Norma de la diferencia entre X1 y x0:', d)

while d > eps and k < 1000:
    print(f'|{k:0.0f} | {X0[0]} {X0[1]} {X0[2]} {X0[3]} | {d:0.4f} |')
    X0 = X1
    X1 = np.dot(B, X0) + c  # siguiente iteración
    k += 1
    d = np.linalg.norm(X1 - X0)  # ||X1 - x0 ||
print(f'|{k:0.0f} | {X0[0]} {X0[1]} {X0[2]} {X0[3]} | {d:0.4f} |')
print('Solución aproximada del sistema por el metodo de Jacobi Ax = b:')
print(X1)

X = np.linalg.solve(A, b)
print('Con solve de numpy es: ', X)

X = np.linalg.inv(A)@b
print('Solución del sistema por la inversa de numpy es:', X)
