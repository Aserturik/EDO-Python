import numpy as np
import matplotlib.pyplot as plt

# Evitar los puntos donde tan(x) no está definida
epsilon = 1e-3
X = np.linspace(-np.pi/2 + epsilon, np.pi/2 - epsilon, 10)
Y = np.tan(X)

def P_n(X, Y, xv):
    n = len(X)
    sum = 0
    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod *= (xv - X[j]) / (X[i] - X[j])
        sum += prod * Y[i]
    return sum

# Graficar
x_vals = np.linspace(-np.pi/2 + epsilon, np.pi/2 - epsilon, 400)
y_vals = [P_n(X, Y, xv) for xv in x_vals]

plt.plot(x_vals, y_vals, label="Polinomio de Lagrange")
plt.plot(x_vals, np.tan(x_vals), '--', label="tan(x)")
plt.scatter(X, Y, color='red', label="Muestras")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Interpolación de Lagrange para tan(x)")
plt.legend()
plt.grid(True)
plt.show()
