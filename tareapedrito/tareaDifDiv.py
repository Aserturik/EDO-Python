import numpy as np
import matplotlib.pyplot as plt


X = np.array([0.5, 1, 2, 4, 8, 12], dtype=float)
Y = np.array([160, 120, 94, 75, 62, 56], dtype=float)

print("Puntos generados:")
print("I:", X)
print("V:", Y)

n = len(X)
D = np.zeros((n, n), dtype=float)
D[:, 0] = Y

for j in range(1, n):
    for i in range(n - j):
        D[i, j] = (D[i + 1, j - 1] - D[i, j - 1]) / (X[i + j] - X[i])


def P_n(X, D, xv):
    n = len(X)
    suma = D[0, 0]
    for i in range(1, n):
        prod = D[0, i]
        for j in range(i):
            prod *= (xv - X[j])
        suma += prod
    return suma


print("\nMatriz de diferencias divididas D:")
for i in range(n):
    for j in range(n-i):
        print(f"D[{i}, {j}]: {D[i, j]:.6f}", end="  ")
    print()

# Mostrar los coeficientes del polinomio de Newton (primera fila de D)
print(f"\nCoeficientes del polinomio de Newton (grado {n-1}):")
for i in range(n):
    print(f"c_{i}: {D[0, i]:.6f}")

# Mostrar el polinomio en forma textual mejorada
print("\nPolinomio P(x) en forma de Newton:")
print(f"P(x) = {D[0, 0]:.3f}", end="")
for i in range(1, n):
    coef = D[0, i]
    if abs(coef) < 1e-10:  # Omitir coeficientes muy pequeños
        continue
    if coef >= 0:
        print(f" + {coef:.3f}", end="")
    else:
        print(f" - {abs(coef):.3f}", end="")

    # Mostrar los términos (x - x_i) en líneas separadas para mejor legibilidad
    print("·", end="")
    for j in range(i):
        if j == 0:
            print(f"(x - {X[j]:.3f})", end="")
        else:
            print(f"·(x - {X[j]:.3f})", end="")

    if i < n-1:  # No añadir nueva línea en el último término
        print()
        print("     ", end="")  # Indentación para alinear términos
print()


