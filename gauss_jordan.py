import numpy as np

A = np.array([
    [-1, 3, 5, 2],
    [1, 9, 8, 4],
    [0, 1, 0, 1],
    [2, 1, 1, -1]
], dtype=float)

b = np.array([10, 15, 2, -3], dtype=float)
B = np.hstack((A, b.reshape(-1, 1)))

print("A = \n", A)
print("b = \n", b)
print("B matriz ampliada = \n", B)


# Paso 1: primera columna
B[0, :] = B[0, :] / B[0, 0]  # F1 -> F1 / B(1,1)
B[1, :] = B[1, :] - B[1, 0] * B[0, :]  # F2 -> F2 - B(2,1) * F1
B[2, :] = B[2, :] - B[2, 0] * B[0, :]  # F3 -> F3 - B(3,1) * F1
B[3, :] = B[3, :] - B[3, 0] * B[0, :]  # F4 -> F4 - B(4,1) * F1

# Paso 2: segunda columna
B[1, :] = B[1, :] / B[1, 1]  # F2 -> F2 / B(2,2)
B[0, :] = B[0, :] - B[0, 1] * B[1, :]  # F1 -> F1 - B(1,2) * F2
B[2, :] = B[2, :] - B[2, 1] * B[1, :]  # F3 -> F3 - B(3,2) * F2
B[3, :] = B[3, :] - B[3, 1] * B[1, :]  # F4 -> F4 - B(4,2) * F2

# Paso 3: tercera columna
B[2, :] = B[2, :] / B[2, 2]  # F3 -> F3 / B(3,3)
B[0, :] = B[0, :] - B[0, 2] * B[2, :]  # F1 -> F1 - B(1,3) * F3
B[1, :] = B[1, :] - B[1, 2] * B[2, :]  # F2 -> F2 - B(2,3) * F3
B[3, :] = B[3, :] - B[3, 2] * B[2, :]  # F4 -> F4 - B(4,3) * F3

# Paso 4: cuarta columna
B[3, :] = B[3, :] / B[3, 3]  # F4 -> F4 / B(4,4)
B[0, :] = B[0, :] - B[0, 3] * B[3, :]  # F1 -> F1 - B(1,4) * F4
B[1, :] = B[1, :] - B[1, 3] * B[3, :]  # F2 -> F2 - B(2,4) * F4
B[2, :] = B[2, :] - B[2, 3] * B[3, :]  # F3 -> F3 - B(3,4) * F4

print("\nMatriz después de Gauss-Jordan:")
print(B)

# Extraer la solución del sistema
gauss_jordan_solucion = B[:, -1]
print("\nSolución del sistema:")
print(f"x1 = {gauss_jordan_solucion[0]:.6f}")
print(f"x2 = {gauss_jordan_solucion[1]:.6f}")
print(f"x3 = {gauss_jordan_solucion[2]:.6f}")
print(f"x4 = {gauss_jordan_solucion[3]:.6f}")
print(f"\nVector solución: x = {gauss_jordan_solucion}")
