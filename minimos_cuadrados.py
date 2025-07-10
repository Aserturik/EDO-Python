import matplotlib.pyplot as plt
import numpy as np

X = np.array([0, 2, 3, 6, 7], dtype=float)  # fuerza x_i (kgf)
Y = np.array([0.120, 0.153, 0.170, 0.225, 0.260],
             dtype=float)  # Estiramientos del resorte (m)
m = len(X)  # Número de puntos


M = np.array([[m, np.sum(X)], [np.sum(X), np.sum(X**2)]],
             dtype=float)  # Matriz de coeficientes

# Vector de términos independientes
b = np.array([np.sum(Y), np.sum(X * Y)], dtype=float)
a = np.linalg.solve(M, b)  # Solución del sistema de ecuaciones


print('Matriz  \n', M)

print('Vector  \n', b)
print('Solución del sistema:  \n', a)


def P_1(a, xval):
    """Función polinómica de primer grado."""
    return a[0] + a[1] * xval


# Graficar con matplotlib


plt.scatter(X, Y, label='Datos', color='blue')

x = np.linspace(min(X), max(X), 100)  # Valores de x para la línea
y = 0*x

for i in range(len(x)):
    y[i] = P_1(a, x[i])

# Graficar la línea de regresión
plt.plot(x, y, label='Regresión lineal', color='red')
plt.xlabel('Fuerza (kgf)')
plt.ylabel('Estiramiento (m)')
plt.title('Regresión lineal de mínimos cuadrados')
plt.legend()
plt.grid()
plt.savefig('minimos_cuadrados.png')
print('Gráfico guardado como minimos_cuadrados.png')
