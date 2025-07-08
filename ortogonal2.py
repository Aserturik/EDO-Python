import numpy as np

A = np.array([[2, 3, 1], [0, 2, 1], [1, 0, 1]], dtype=float)
# b = np.array([[0], [0]], dtype=float)
b = np.array([[0], [1], [0]], dtype=float)
B = np.hstack((A, b))  # Matriz ampliada

print("Matriz A:\n", A)
print("Vector b:\n", b)
print("Matriz ampliada B:\n", B)

rango_A = np.linalg.matrix_rank(A)
rango_B = np.linalg.matrix_rank(B)

dim_A = np.shape(A)
n_incognitas = dim_A[1]
print(f"Rango de A: {rango_A}")
print(f"Rango de B: {rango_B}")
print('Número de incógnitas:', n_incognitas)

if rango_A == rango_B == n_incognitas:
    print("El sistema tiene una única solución.")
    x = np.linalg.solve(A, b)
    print("Solución del sistema:", x)
elif rango_A == rango_B < n_incognitas:
    print("El sistema tiene infinitas soluciones.")
    x = np.linalg.solve(A, b)
    # Para encontrar una solución particular, podemos usar la función lstsq
    # x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
    # print("Solución particular del sistema:", x)
elif rango_A < rango_B:
    print("El sistema es inconsistente y no tiene solución.")
else:
    print("El sistema no tiene solución única ni infinitas soluciones.")
