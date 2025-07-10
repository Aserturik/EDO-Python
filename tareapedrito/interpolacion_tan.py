import matplotlib.pyplot as plt
import numpy as np

# 1. Generar 10 valores aleatorios de x en el intervalo abierto (-π/2, π/2)
# Evitamos valores muy cercanos a ±π/2 donde tan(x) tiende a infinito
x_min = -np.pi/2 + 0.1  # Evitar singularidades
x_max = np.pi/2 - 0.1
x_points = np.random.uniform(x_min, x_max, 10)
x_points = np.sort(x_points)  # Ordenar para mejor visualización

# 2. Calcular los valores correspondientes de y = tan(x)
y_points = np.tan(x_points)

print("Puntos generados:")
print("X:", x_points)
print("Y = tan(X):", y_points)

# 3. Ajustar polinomio de grado 9 usando el método de matriz (como en aprox_poli_simple.py)
n = len(x_points)  # número de puntos (10)
degree = n - 1     # grado del polinomio (9)

# Crear matriz C donde C[i][j] = x_points[i]^j
C = np.zeros((n, n), dtype=float)  # matriz nula de orden n
for i in range(n):
    C[:, i] = x_points**i  # llenamos la matriz con las potencias de x

# Resolver el sistema C*A = Y para encontrar los coeficientes A
A = np.linalg.solve(C, y_points)  # resolvemos el sistema C*A=Y

print(f"\nCoeficientes del polinomio de grado {degree}:")
for i, coef in enumerate(A):
    print(f"a_{i}: {coef:.6f}")

# 4. Mostrar el polinomio en forma textual
print("\nPolinomio P(x) en forma textual:")
print("P(x) =", end=" ")
for i, coef in enumerate(A):
    if i > 0 and coef >= 0:
        print(" +", end=" ")
    elif coef < 0:
        print(" -", end=" ")
        coef = abs(coef)
    if i == 0:
        print(f"{coef:.6f}", end="")
    elif i == 1:
        print(f"{coef:.6f}*x", end="")
    else:
        print(f"{coef:.6f}*x^{i}", end="")
print()

# Función del polinomio para evaluación (como en aprox_poli_simple.py)


def P_n(A, x):
    """Polinomio de grado n"""
    s = 0
    for i in range(n):
        s += A[i] * (x**i)  # sumamos los términos del polinomio
    return s


# 5. Crear valores densos para las gráficas suaves
x_dense = np.linspace(x_min, x_max, 1000)
y_polynomial = P_n(A, x_dense)
y_tan_real = np.tan(x_dense)

# 6. Crear la gráfica completa con el estilo mejorado
plt.figure(figsize=(12, 8))

# Diagrama de dispersión de los puntos originales
plt.scatter(x_points, y_points, color='red', s=80, zorder=5,
            label='Puntos de datos (x, tan(x))', edgecolors='black', linewidth=1)

# Mostrar las coordenadas de cada punto en la gráfica
for x, y in zip(x_points, y_points):
    plt.annotate(f"({x:.2f}, {y:.2f})", (x, y), textcoords="offset points", xytext=(5, 5),
                 fontsize=9, color='black', bbox=dict(boxstyle='round,pad=0.15', fc='white', alpha=0.7), zorder=6)

# Curva del polinomio interpolante
plt.plot(x_dense, y_polynomial, color='blue', linewidth=2,
         label=f'Polinomio interpolante de grado {degree}', linestyle='-')

# Función real tan(x)
plt.plot(x_dense, y_tan_real, color='green', linewidth=2,
         label='Función real tan(x)', linestyle='--', alpha=0.8)

# Configuración de la gráfica
plt.title('Interpolación Polinómica de y = tan(x)',
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
plt.savefig('interpolacion_tan_mejorada.png', dpi=300, bbox_inches='tight')
print("\nGráfica guardada como 'interpolacion_tan_mejorada.png'")

# 7. Análisis del error
y_polynomial_at_points = P_n(A, x_points)
error = np.abs(y_points - y_polynomial_at_points)

# 8. Mostrar algunos valores del polinomio vs función real
print("\nComparación de valores:")
print("x\t\ttan(x)\t\tP(x)\t\tError")
print("-" * 50)
test_points = np.linspace(x_min, x_max, 5)
for x_test in test_points:
    tan_val = np.tan(x_test)
    poly_val = P_n(A, x_test)
    error_val = abs(tan_val - poly_val)
    print(f"{x_test:.3f}\t\t{tan_val:.6f}\t{poly_val:.6f}\t{error_val:.6f}")
