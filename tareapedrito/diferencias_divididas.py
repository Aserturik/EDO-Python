# Metodo de Newton en diferencias divididas

import numpy as np


X = np.array([0.5, 1, 2, 4, 8, 12], dtype=float)
Y = np.array([160, 120, 94, 75, 62, 56], dtype=float)

n = len(X)  # Numero de puntos
D = np.zeros((n, n))  # Matriz de diferencias divididas

D[:, 0] = Y  # Primera columna con los valores de Y

for i in range(n - 1):
    for j in range(n - i - 1):
        D[j][i + 1] = (D[j + 1][i] - D[j][i]) / (X[j + i + 1] - X[j])


print(D)
