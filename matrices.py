import numpy as np

A = np.array([[1, -1, 3, 5], [2, 5, 7, 9], [-3, 0, 7, 5]], dtype=float)
# dimA = np.shape(A)
print("Matriz A:")
print(A)
# print("Dmensiones de A:", dimA)
# print('La colunma 3 de la matriz A es:', A[:, 2])
# print('La fila 2 de la matriz A es:', A[1, :])

# Matriz B
B = A.copy()
print("\nMatriz B:")
B[0, 1] = 10
print(B)

# Multipilicación de matrices
# C = np.dot(A, B)
# print("\nMatriz C (producto de A y B):")
# print(C)

# Transposición de matrices
D = np.transpose(B)
print("\nMatriz D (transpuesta de B):")
print(D)

# Multiplicación de A con D
E = np.dot(A, D)
print("\nMatriz E (producto de A y D):")
print(E)

# Matriz identidad
F = np.eye(5)
print("\nMatriz identidad I:")
print(F)

# Matriz de unos
G = np.ones((5, 5))
print("\nMatriz de unos G:")
print(G)

# Matriz de ceros
H = np.zeros((5, 5))
print("\nMatriz de ceros H:")
print(H)

# Matriz de dieses
diez = 10*np.ones((5, 5))
print("\nMatriz de dieses:")
print(diez)

# Matriz Inversa
F = np.array([[1, 2, 3], [-1, 3, 5], [4, 8, 7]], dtype=float)
FI = np.linalg.inv(F)
print("\nMatriz F:")
print(F)
print("\nMatriz inversa de F:")
print(FI)

print('F por F^-1')
# Verificación de la inversa
FFI = np.dot(F, FI)
print(FFI)
