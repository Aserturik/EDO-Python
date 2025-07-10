import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, simplify, expand

# Intervalo sin asíntotas
a = -np.pi/2 + 0.1
b = np.pi/2 - 0.1

# 10 puntos equiespaciados
X = np.linspace(a, b, 10)
Y = np.tan(X)

# Construcción de la matriz de Vandermonde
n = len(X)
C = np.zeros((n, n))
for i in range(n):
    C[:, i] = X**i

# Resolver el sistema lineal
A = np.linalg.solve(C, Y)

# Polinomio como función


def P_n(A, x):
    return sum(A[i] * x**i for i in range(len(A)))


# Gráfica
plt.figure(figsize=(10, 6))
plt.scatter(X, Y, color='red', label='Datos')
x_vals = np.linspace(a, b, 300)
y_vals = [P_n(A, x) for x in x_vals]
plt.plot(x_vals, y_vals, label='Polinomio interpolante', color='blue')
plt.plot(x_vals, np.tan(x_vals), label='tan(x)',
         linestyle='dashed', color='green')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Interpolación polinómica de tan(x)")
plt.grid(True)
plt.savefig("interpolacion_polinomica_tan.png")

# Mostrar el polinomio en forma simbólica
x = symbols('x')
polinomio = sum(A[i]*x**i for i in range(n))
polinomio_simplificado = simplify(expand(polinomio))

print("Polinomio P(x):")
for i in range(n):
    coef = round(A[i], 6)
    if coef != 0:
        print(f"{'+ ' if coef >= 0 and i > 0 else ''}{coef}·x^{i}" if i >
              0 else f"{coef}", end=' ')
print()
