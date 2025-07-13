import numpy as np
import matplotlib.pyplot as plt

X = np.array([0.5, 1, 2, 4, 8, 12], dtype=float)
Y = np.array([160, 120, 94, 75, 62, 56], dtype=float)

n = len(X)
D = np.zeros((n, n), dtype=float)
D[:, 0] = Y


for j in range(1, n):
    for i in range(n - j):
        D[i, j] = (D[i + 1, j - 1] - D[i, j - 1]) / (X[i + j] - X[i])


def P_n(x, X, D):
    n = len(X)
    resultado = D[0, 0]

    for i in range(1, n):
        producto = 1.0
        for j in range(i):
            producto *= (x - X[j])
        resultado += D[0, i] * producto

    return resultado


print("\nMatriz de diferencias divididas D:")
for i in range(n):
    for j in range(n-i):
        print(f"D[{i}, {j}]: {D[i, j]:.6f}", end="  ")
    print()

print(f"\nCoeficientes del polinomio de Newton (grado {n-1}):")
for i in range(n):
    print(f"c_{i}: {D[0, i]:.6f}")


print("\nPolinomio de Newton (forma simbólica):")
polynomial_str = f"{D[0, 0]:.4f}"
for i in range(1, n):
    polynomial_str += f" + {D[0, i]:.4f}"
    for j in range(i):
        polynomial_str += f"*(x - {X[j]})"
print(polynomial_str)

i_x = 7
i_y = P_n(i_x, X, D)
print('\nInterpolación polinómica de 7:', i_y)
print(f'P({i_x}) = {i_y:.2f}')


plt.scatter(X, Y, color='red', label='Datos')
plt.scatter(i_x, i_y, color='blue',
            label=f'Punto Interpolado ({i_x}, {i_y:.2f})')
plt.text(i_x, i_y, f"({i_x}, {i_y:.2f})", fontsize=8)
x_vals = np.linspace(min(X), max(X), 200)
y_vals = [P_n(x, X, D) for x in x_vals]
plt.plot(x_vals, y_vals, label='Polinomio')
for i in range(len(X)):
    plt.text(X[i], Y[i], f"({X[i]:.0f}, {Y[i]:.2f})", fontsize=8)
plt.xlabel('I')
plt.ylabel('V')
plt.legend()
plt.title('Metodo de deferencias divididas')
plt.savefig("parcial-alex.png")
