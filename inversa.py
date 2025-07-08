import numpy as np

# Definición del sistema de ecuaciones lineales Ax = b
A = np.array([
    [-1, 3, 5, 2],
    [1, 9, 8, 4],
    [0, 1, 0, 1],
    [2, 1, 1, -1]
], dtype=float)

b = np.array([10, 15, 2, -3], dtype=float)

print("Matriz A:")
print(A)
print("\nVector b:")
print(b)

# Crear la matriz identidad 4x4
I = np.eye(4, dtype=float)

# Crear la matriz aumentada [A|I] para calcular la inversa
B = np.hstack((A, I))

# PASO 1: Primera columna
B[0, :] = B[0, :] / B[0, 0]  # F1 -> F1 / B(1,1)
B[1, :] = B[1, :] - B[1, 0] * B[0, :]  # F2 -> F2 - B(2,1) * F1
B[2, :] = B[2, :] - B[2, 0] * B[0, :]  # F3 -> F3 - B(3,1) * F1
B[3, :] = B[3, :] - B[3, 0] * B[0, :]  # F4 -> F4 - B(4,1) * F1

# PASO 2: Segunda columna
B[1, :] = B[1, :] / B[1, 1]  # F2 -> F2 / B(2,2)
B[0, :] = B[0, :] - B[0, 1] * B[1, :]  # F1 -> F1 - B(1,2) * F2
B[2, :] = B[2, :] - B[2, 1] * B[1, :]  # F3 -> F3 - B(3,2) * F2
B[3, :] = B[3, :] - B[3, 1] * B[1, :]  # F4 -> F4 - B(4,2) * F2

# PASO 3: Tercera columna
B[2, :] = B[2, :] / B[2, 2]  # F3 -> F3 / B(3,3)
B[0, :] = B[0, :] - B[0, 2] * B[2, :]  # F1 -> F1 - B(1,3) * F3
B[1, :] = B[1, :] - B[1, 2] * B[2, :]  # F2 -> F2 - B(2,3) * F3
B[3, :] = B[3, :] - B[3, 2] * B[2, :]  # F4 -> F4 - B(4,3) * F3

# PASO 4: Cuarta columna
B[3, :] = B[3, :] / B[3, 3]  # F4 -> F4 / B(4,4)
B[0, :] = B[0, :] - B[0, 3] * B[3, :]  # F1 -> F1 - B(1,4) * F4
B[1, :] = B[1, :] - B[1, 3] * B[3, :]  # F2 -> F2 - B(2,4) * F4
B[2, :] = B[2, :] - B[2, 3] * B[3, :]  # F3 -> F3 - B(3,4) * F4

# Extraer la matriz inversa A^(-1) de las columnas 4-7 de la matriz aumentada
A_inv = B[:, 4:8]

# Multiplicar A^(-1) * b manualmente
inversa_solucion = np.zeros(4)
for i in range(4):
    for j in range(4):
        inversa_solucion[i] += A_inv[i, j] * b[j]

print("\nSolución del sistema usando matriz inversa:")
print(f"x1 = {inversa_solucion[0]:.6f}")
print(f"x2 = {inversa_solucion[1]:.6f}")
print(f"x3 = {inversa_solucion[2]:.6f}")
print(f"x4 = {inversa_solucion[3]:.6f}")
print(f"\nVector solución: x = {inversa_solucion}")

# Verificación: Ax = b
print("\n=== VERIFICACIÓN ===")
verificacion = np.zeros(4)
for i in range(4):
    for j in range(4):
        verificacion[i] += A[i, j] * inversa_solucion[j]

print("Verificación (Ax):")
print(verificacion)
print("\nVector b original:")
print(b)

# Calcular la diferencia |Ax - b|
diferencia = 0
for i in range(4):
    diferencia += (verificacion[i] - b[i])**2
diferencia = diferencia**0.5

print(f"\nDiferencia |Ax - b|: {diferencia:.10f}")
