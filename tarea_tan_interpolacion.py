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

# 3. Ajustar polinomio de grado 9 usando regresión polinómica
degree = 9
coefficients = np.polyfit(x_points, y_points, degree)
polynomial = np.poly1d(coefficients)

print(f"\nCoeficientes del polinomio de grado {degree}:")
for i, coef in enumerate(coefficients):
    print(f"a_{degree-i}: {coef:.6f}")

# 4. Crear valores densos para las gráficas suaves
x_dense = np.linspace(x_min, x_max, 1000)
y_polynomial = polynomial(x_dense)
y_tan_real = np.tan(x_dense)

# 5. Crear la gráfica completa
plt.figure(figsize=(12, 8))

# Diagrama de dispersión de los puntos originales
plt.scatter(x_points, y_points, color='red', s=80, zorder=5,
            label='Puntos de datos (x, tan(x))', edgecolors='black', linewidth=1)

# Mostrar las coordenadas de cada punto en la gráfica
for x, y in zip(x_points, y_points):
    plt.annotate(f"({x:.2f}, {y:.2f})", (x, y), textcoords="offset points", xytext=(5, 5),
                 fontsize=9, color='black', bbox=dict(boxstyle='round,pad=0.15', fc='white', alpha=0.7), zorder=6)

# Curva del polinomio ajustado
plt.plot(x_dense, y_polynomial, color='blue', linewidth=2,
         label=f'Polinomio de grado {degree}', linestyle='-')

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
plt.savefig('interpolacion_tangente.png', dpi=300, bbox_inches='tight')
print("\nGráfica guardada como 'interpolacion_tangente.png'")

# 6. Análisis del error
y_polynomial_at_points = polynomial(x_points)
error = np.abs(y_points - y_polynomial_at_points)
max_error = np.max(error)
mean_error = np.mean(error)

print("\nAnálisis del error:")
print(f"Error máximo: {max_error:.6f}")
print(f"Error promedio: {mean_error:.6f}")
print(f"Error relativo promedio: {
      mean_error/np.mean(np.abs(y_points))*100:.2f}%")
