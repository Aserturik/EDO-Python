import numpy as np
import matplotlib.pyplot as plt

# Datos
X = np.array([280, 650, 1000, 1200, 1500, 1700], dtype=float)
Y = np.array([32.7, 45.4, 52.15, 53.7, 52.9, 50.3], dtype=float)
m = len(X)

# Construcción de la matriz del sistema normal para ajuste cuadrático
matriz = np.array([
    [m,           np.sum(X),        np.sum(X**2)],
    [np.sum(X),   np.sum(X**2),     np.sum(X**3)],
    [np.sum(X**2), np.sum(X**3),     np.sum(X**4)]
], dtype=float)

# Vector de términos independientes
b = np.array([
    [np.sum(Y)],
    [np.sum(X * Y)],
    [np.sum(X**2 * Y)]
], dtype=float)

# Resolución del sistema para obtener coeficientes a0, a1, a2
a = np.linalg.solve(matriz, b)

# Mostrar resultados
print('Matriz del sistema:\n', matriz)
print('Términos independientes:\n', b)
print('Coeficientes a0, a1, a2:\n', a)

# Definir el polinomio cuadrático


def P_2(a, xval):
    return a[0][0] + a[1][0]*xval + a[2][0]*xval**2


# Graficar
x_vals = np.linspace(min(X) - 100, max(X) + 100, 300)
y_vals = [P_2(a, xv) for xv in x_vals]

plt.plot(x_vals, y_vals, label="Ajuste cuadrático")
plt.scatter(X, Y, color='red', label="Puntos originales")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Ajuste Cuadrático por Mínimos Cuadrados")
plt.grid(True)


for i in range(len(X)):
    plt.text(X[i], Y[i], f"({X[i]:.0f}, {Y[i]:.2f})", fontsize=8)

plt.legend()
plt.savefig('hola.png')
