import matplotlib.pyplot as plt
import numpy as np

# Presion tomando 2 puntos
X = np.array([1, 5], dtype=float)
# Temperaturas correspondientes a los puntos
Y = np.array([56.5, 113], dtype=float)

# Sistema de ecuaciones para encontrar los coeficientes del polinomio de primer grado
M = np.array([[1, 1], [X[0], X[1]]], dtype=float)

# Vector de resultados
A = np.linalg.solve(M, Y)


def p_1(a0, a1, x):
    """Polinomio de primer grado"""
    return a0 + a1 * x


y0 = p_1(A[0], A[1], 1)
y1 = p_1(A[0], A[1], 5)

print(f'presion en T=1: {y0}')
print(f'presion en T=5: {y1}')

# Temperatura a interpolar en T=2
yp = p_1(A[0], A[1], 2)  # interpolación en T=2
print(f'Interpolación en T=2: {yp}')

# ----------------------------------------
# Presion tomando 7 puntos
X = np.array([1, 2, 5, 10, 20, 30, 40], dtype=float)  # presion
# Temperaturas correspondientes a los puntos
Y = np.array([56.5, 78.6, 113, 114.5, 181, 205, 214],
             dtype=float)  # temperatura
n = len(X)
C = np.zeros((n, n), dtype=float)  # matriz nula de orden n

for i in range(n):
    C[:][i] = X**i  # llenamos la matriz con las potencias de x

A = np.linalg.solve(C.T, Y)  # resolvemos el sistema C*A=Y


def P_n(A, x):
    """Polinomio de grado n"""
    s = 0
    for i in range(n):
        s += A[i] * (x**i)  # sumamos los terminos del polinomio

    return s


print(X)  # puntos de presion
print(P_n(A, X))  # presion en los puntos de X
print(P_n(A, 2))  # presion en T=2


# Grafica de el sistema con matplotlib

# Crear puntos para la gráfica
x_values = np.linspace(1, 41, 100)
y_values = P_n(A, x_values)
# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Polinomio de interpolación', color='blue')
plt.scatter(X, Y, color='red', label='Puntos de datos')
plt.title('Interpolación Polinómica')
plt.xlabel('Presión')
plt.ylabel('Temperatura')
plt.legend()
plt.grid()
plt.savefig('interpolacion_polinomica.png')  # Guardar la gráfica


# Tarea
# y = tan(x)
# x = 10 puntos entre (-pi/2 y pi/2)

# X | x0 | x1 | x2 | x3 | x4 | x5 | x6 | x7 | x8 | x9 |
# ---
# Y = tan(x)
# encontrar los coeficientes del polinomio de grado 9

# 2. Graficar el diagrama de dispersión de los puntos y la curva del polinomio

# 3 graficar la funcion y = tan(x) en el mismo rango de x
# Superponer la gráfica del polinomio con la función y = tan(x)
