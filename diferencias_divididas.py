# Metodo de Newton en diferencias divididas

import numpy as np


X = np.array([-2, -1, 0, 2], dtype=float)
Y = np.array([-18, -5, -2, -2], dtype=float)

n = len(X)  # Numero de puntos
D = np.zeros((n, n))  # Matriz de diferencias divididas

D[:, 0] = Y  # Primera columna con los valores de Y
# D[0][1] = (D[1][0] - D[0][0]) / (X[1] - X[0])  # Primera diferencia dividida
# D[1][1] = (D[2][0] - D[1][0]) / (X[2] - X[1])  # Segunda diferencia dividida
# D[2][1] = (D[3][0] - D[2][0]) / (X[3] - X[2])  # Tercera diferencia dividida

for i in range(n - 1):
    for j in range(n - i - 1):
        D[j][i + 1] = (D[j + 1][i] - D[j][i]) / (X[j + i + 1] - X[j])


print(D)
