import numpy as np
import cmath as cm

a4, a3, a2, a1, a0, k, x0, eps, d = 4, 3, -2, 4, -8, 0, 0, 0.0001, 10
print(f"Polinomio: {a4}x^4 + {a3}x^3 + {a2}x^2 + {a1}x + {a0}")
print("Metodo de Newton-Raphson para encontrar raices")
print(f"Tolerancia: {eps}, Iteraciones maximas: {d}")
print("-" * 50)
# Metodo de Newton-Raphson
print(f'Iteracion {k}: x0 = {x0:0.4f}')

while d > k:
    # División sintética para evaluar f(x0)
    b4 = a4
    b3 = a3 + b4 * x0
    b2 = a2 + b3 * x0
    b1 = a1 + b2 * x0
    b0 = a0 + b1 * x0

    # División sintética para evaluar f'(x0)
    c4 = b4
    c3 = b3 + c4 * x0
    c2 = b2 + c3 * x0
    c1 = b1 + c2 * x0

    # Aplicar fórmula de Newton-Raphson
    x1 = x0 - b0 / c1
    k += 1

    error = abs(x1 - x0)
    print(f'Iteracion {k}: x = {x1:0.6f}, f(x) = {b0:0.6f}, '
          f'error = {error:0.6f}')

    # Verificar convergencia
    if error < eps:
        print(f'Convergencia alcanzada en {k} iteraciones')
        print(f'Raiz aproximada: x = {x1:0.6f}')
        break

    x0 = x1

if k >= d:
    print(f'Máximo de iteraciones ({d}) alcanzado')
    print(f'Raiz aproximada: x = {x1:0.4f}')

a3, a2, a1, a0, k, x0, eps, d = b4, b3, b2, b1, 0, 0, 0.0001, 10
print("\nReiniciando con un nuevo polinomio de grado 3")

print(f"Polinomio: {a3}x^3 + {a2}x^2 + {a1}x + {a0}")
print("Metodo de Newton-Raphson para encontrar raices")
print(f"Tolerancia: {eps}, Iteraciones maximas: {d}")


# Metodo de Newton-Raphson para polinomio de grado 3
print(f'Iteracion {k}: x0 = {x0:0.4f}')
while k < d:
    # División sintética para evaluar f(x0)
    b3 = a3
    b2 = a2 + b3 * x0
    b1 = a1 + b2 * x0
    b0 = a0 + b1 * x0

    # División sintética para evaluar f'(x0)
    c3 = b3
    c2 = b2 + c3 * x0
    c1 = b1 + c2 * x0

    # Aplicar fórmula de Newton-Raphson
    x1 = x0 - b0 / c1
    k += 1

    error = abs(x1 - x0)
    print(f'Iteracion {k}: x = {x1:0.6f}, f(x) = {b0:0.6f}, '
          f'error = {error:0.6f}')

    # Verificar convergencia
    if error < eps:
        print(f'Convergencia alcanzada en {k} iteraciones')
        print(f'Raiz aproximada: x = {x1:0.6f}')
        break

    x0 = x1

if k >= d:
    print(f'Máximo de iteraciones ({d}) alcanzado')
    print(f'Raiz aproximada: x = {x1:0.4f}')

# Reiniciar variables para el siguiente polinomio
print("\nReiniciando con un nuevo polinomio de grado 2")
print("Formula cuadratica para encontrar raices")

x3 = (-b2 + cm.sqrt(b2**2 - 4*b3*b1)) / (2*b3)
x4 = (-b2 - cm.sqrt(b2**2 - 4*b3*b1)) / (2*b3)

print(f'x3 = {x3.real:0.6f} + {x3.imag:0.6f}j')
print(f'x4 = {x4.real:0.6f} + {x4.imag:0.6f}j')
