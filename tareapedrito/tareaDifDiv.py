# Tomar 10 muestras de la tangente en el intervalo [-pi/2, pi/2]
# Metodo de Newton en diferencias divididas para interpolación polinómica
import numpy as np
import matplotlib.pyplot as plt

# 1. Generar 10 valores aleatorios de x en el intervalo abierto (-π/2, π/2)
# Evitamos valores muy cercanos a ±π/2 donde tan(x) tiende a infinito
x_min = -np.pi/2 + 0.001  # Evitar singularidades más conservadoramente
x_max = np.pi/2 - 0.001
X = np.random.uniform(x_min, x_max, 10)
X = np.sort(X)  # Ordenar para mejor visualización

# 2. Calcular los valores correspondientes de y = tan(x)
Y = np.tan(X)

print("Puntos generados:")
print("X:", X)
print("Y = tan(X):", Y)

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

# 5. Crear valores densos para las gráficas suaves
x_dense = np.linspace(x_min, x_max, 1000)
y_polynomial = [P_n(X, D, xv) for xv in x_dense]
y_tan_real = np.tan(x_dense)

# 6. Crear la gráfica completa con el estilo mejorado
plt.figure(figsize=(12, 8))

# Diagrama de dispersión de los puntos originales
plt.scatter(X, Y, color='red', s=80, zorder=5,
            label='Puntos de datos (x, tan(x))', edgecolors='black', linewidth=1)

# Mostrar las coordenadas de cada punto en la gráfica
for x, y in zip(X, Y):
    plt.annotate(f"({x:.2f}, {y:.2f})", (x, y), textcoords="offset points", xytext=(5, 5),
                 fontsize=9, color='black', bbox=dict(boxstyle='round,pad=0.15', fc='white', alpha=0.7), zorder=6)

# Curva del polinomio interpolante
plt.plot(x_dense, y_polynomial, color='blue', linewidth=2,
         label=f'Polinomio de Newton (grado {n-1})', linestyle='-')

# Función real tan(x)
plt.plot(x_dense, y_tan_real, color='green', linewidth=2,
         label='Función real tan(x)', linestyle='--', alpha=0.8)

# Configuración de la gráfica
plt.title('Interpolación de Newton - Diferencias Divididas para y = tan(x)',
          fontsize=16, fontweight='bold')
plt.xlabel('x (radianes)', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11, loc='upper left')

# Establecer límites del eje y para mejor visualización
plt.ylim(-10, 10)

# Añadir líneas verticales en ±π/2 para mostrar las asíntotas
plt.axvline(-np.pi/2, color='gray', linestyle=':',
            alpha=0.5, label='Asíntotas tan(x)')
plt.axvline(np.pi/2, color='gray', linestyle=':', alpha=0.5)

# Añadir marcas en π/2 y -π/2 en el eje x
pi_ticks = [-np.pi/2, -np.pi/4, 0, np.pi/4, np.pi/2]
pi_labels = [r'$-\frac{\pi}{2}$', r'$-\frac{\pi}{4}$',
             '0', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$']
plt.xticks(pi_ticks, pi_labels)

plt.tight_layout()
plt.savefig('diferencias_divididas.png',
            dpi=300, bbox_inches='tight')
print("\nGráfica guardada como 'diferencias_divididas.png'")

# 7. Análisis del error
y_polynomial_at_points = [P_n(X, D, x) for x in X]
error = np.abs(Y - y_polynomial_at_points)

# 8. Mostrar algunos valores del polinomio vs función real
print("\nComparación de valores:")
print("x\t\ttan(x)\t\tP(x)\t\tError")
print("-" * 50)
test_points = np.linspace(x_min, x_max, 5)
for x_test in test_points:
    tan_val = np.tan(x_test)
    poly_val = P_n(X, D, x_test)
    error_val = abs(tan_val - poly_val)
    print(f"{x_test:.3f}\t\t{tan_val:.6f}\t{poly_val:.6f}\t{error_val:.6f}")
