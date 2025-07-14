# edo por metdodo de Euler
import numpy as np


def F(x, y):
    return x - y


x0, xf, n = 0, 1, 5

h = (xf-x0)/n

x = np.linspace(x0, xf, n+1)  # n+1 puntos para incluir xf
y = 0*x

y[0] = 2

for k in range(1, n):
    y[k+1] = y[k] + F(x[k], y[k]) * h  # Método de Euler explícito

print("x:", x)
print("y:", y)

# tarea: hacer la grafica de los puntos y la gráfica de la solucion
# Solucion numerica y solucion analitica
