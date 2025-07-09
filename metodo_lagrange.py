import matplotlib.pyplot as plt
import numpy as np

# Metodo para ajustar un conjunto de n+1 puntos a un polinomio de grado n

X = np.array([-3, 0, 5, 7], dtype=float)
Y = np.array([0, 1, 3, 6], dtype=float)


def P_n(X, Y, xv):
    """Calcula el polinomio de Lagrange para un conjunto de
    puntos (X, Y) en xv."""
    n = len(X)  # Numero de puntos
    L = 0*X  # Inicializa el vector Lagrange
    suma = 0  # Inicializa la suma de los terminos
    for k in range(n):
        prod_N, prod_D = 1, 1  # Productoria del denominador y numerador
        for i in range(n):
            if i != k:
                prod_N *= (xv - X[i])
                prod_D *= (X[k] - X[i])
        L[k] = prod_N / prod_D  # Lagrange
        suma += L[k] * Y[k]  # Suma de los terminos

    return suma  # Retorna el valor del polinomio en xv


yv = P_n(X, Y, 1.8)
print(yv)

# Grafica el polinomio de Lagrange
plt.scatter(X, Y, label='Puntos dados', color='blue',
            marker='o')  # Puntos originales
x = np.linspace(min(X)-1, max(X)+1, 100)  # Valores de x para la grafica
y = [P_n(X, Y, xv) for xv in x]  # Calcula el polinomio en los valores de x
for k in range(len(X)):
    prod_N, prod_D = 1, 1  # Productoria del denominador y numerador
    for i in range(len(X)):
        y[k] = P_n(X, Y, x[k])  # Calcula el valor del polinomio en x[k]


# Grraficar la funcion
plt.plot(x, y, label='Polinomio de Lagrange', color='red')
plt.title('Polinomio de Lagrange')
plt.xlabel('x')
plt.ylabel('P_n(x)')
plt.legend()
plt.grid(True)

for i in range(len(X)):
    xi = f"{X[i]:.2f}"
    yi = f"{Y[i]:.2f}"
    punto = '(' + xi + ', ' + yi + ')'
    plt.text(X[i], Y[i], punto, fontsize=9,
             ha='right', va='bottom', color='blue')


# Guardar la grafica
plt.savefig('metodo_lagrange.png')
