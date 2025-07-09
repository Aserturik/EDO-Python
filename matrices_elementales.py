import numpy as np


def permutation_matrix(n, i, j):
    P = np.eye(n, dtype=float)
    P[i, i] = 0
    P[j, j] = 0
    P[i, j] = 1
    P[j, i] = 1
    return P


def scaling_matrix(n, i, k):
    M = np.eye(n, dtype=float)
    M[i, i] = k
    return M


def substitution_matrix(n, i, j, k):
    S = np.eye(n, dtype=float)
    S[i, j] = k
    return S


# Definir la matriz A y el vector b
A = np.array([
    [-1, 3, 5, 2],
    [1, 9, 8, 4],
    [0, 1, 0, 1],
    [2, 1, 1, -1]
], dtype=float)

b = np.array([10, 15, 2, -3], dtype=float)

# Crear la matriz aumentada [A | b]
n = A.shape[0]
Ab = np.hstack([A, b.reshape(-1, 1)])

# Eliminación hacia adelante
for col in range(n):
    # Normalizar el pivote en la fila actual
    pivot = Ab[col, col]
    if pivot == 0:
        # Buscar una fila con pivote no nulo para intercambiar
        for k in range(col + 1, n):
            if Ab[k, col] != 0:
                P = permutation_matrix(n, col, k)
                Ab = P @ Ab
                pivot = Ab[col, col]
                break
        else:
            raise ValueError(
                f"No se encontró pivote no nulo en la columna {col}")
    if pivot != 1:
        M = scaling_matrix(n, col, 1 / pivot)
        Ab = M @ Ab

    # Hacer ceros debajo del pivote
    for row in range(col + 1, n):
        if Ab[row, col] != 0:
            factor = -Ab[row, col]
            S = substitution_matrix(n, row, col, factor)
            Ab = S @ Ab

# Eliminación hacia atrás
for col in range(n - 1, -1, -1):
    for row in range(col - 1, -1, -1):
        if Ab[row, col] != 0:
            factor = -Ab[row, col]
            S = substitution_matrix(n, row, col, factor)
            Ab = S @ Ab

# Extraer la solución
x = Ab[:, -1]

# Imprimir resultados
print("Solución del sistema x:")
print(x)
