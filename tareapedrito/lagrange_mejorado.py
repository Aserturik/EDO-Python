"""
Método de Interpolación de Lagrange para función tan(x)
Versión mejorada con visualización profesional
"""

import numpy as np
import matplotlib.pyplot as plt

# 1. Configuración inicial
np.random.seed(42)  # Para reproducibilidad
n_puntos = 10

# Rango seguro para evitar singularidades de tan(x) en ±π/2
x_min = -np.pi/2 + 0.1
x_max = np.pi/2 - 0.1

# 2. Generación de puntos aleatorios ordenados
X = np.sort(np.random.uniform(x_min, x_max, n_puntos))
Y = np.tan(X)

print("Puntos generados:")
for i, (x, y) in enumerate(zip(X, Y)):
    print(f"  ({x:.6f}, {y:.6f})")

# 3. Implementación del método de Lagrange


def P_n(X, Y, xv):
    """
    Polinomio de interpolación de Lagrange
    """
    n = len(X)
    sum_val = 0
    for i in range(n):
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (xv - X[j]) / (X[i] - X[j])
        sum_val += L_i * Y[i]
    return sum_val


# 4. Calcular coeficientes del polinomio en forma estándar
def calcular_coeficientes(X, Y):
    """
    Calcula los coeficientes del polinomio en forma estándar.
    a₀ + a₁x + a₂x² + ...
    """
    n = len(X)
    coeficientes = np.zeros(n)
    
    for i in range(n):
        # Calcular coeficientes del i-ésimo término de Lagrange
        temp_coef = np.zeros(n)
        temp_coef[0] = Y[i]
        
        # Construir el polinomio Li(x) = Y[i] * ∏(x-X[j])/(X[i]-X[j])
        denominador = 1
        for j in range(n):
            if i != j:
                denominador *= (X[i] - X[j])
        
        # Numerador: ∏(x - X[j]) para j ≠ i
        numerador_coef = np.array([1.0])
        for j in range(n):
            if i != j:
                # Multiplicar por (x - X[j])
                nuevo_coef = np.zeros(len(numerador_coef) + 1)
                nuevo_coef[1:] += numerador_coef
                nuevo_coef[:-1] -= X[j] * numerador_coef
                numerador_coef = nuevo_coef
        
        # Dividir por denominador y multiplicar por Y[i]
        Li_coef = (Y[i] / denominador) * numerador_coef
        
        # Sumar al polinomio total
        for k in range(len(Li_coef)):
            if k < len(coeficientes):
                coeficientes[k] += Li_coef[k]
    
    return coeficientes


coeficientes = calcular_coeficientes(X, Y)

print("\nCoeficientes del polinomio:")
for i, coef in enumerate(coeficientes):
    print(f"  a_{i} = {coef:.6f}")

print("\nPolinomio de Lagrange:")
terminos = []
for i, coef in enumerate(coeficientes):
    if abs(coef) > 1e-10:  # Solo mostrar términos significativos
        if i == 0:
            terminos.append(f"{coef:.3f}")
        elif i == 1:
            if coef >= 0 and terminos:
                terminos.append(f" + {coef:.3f}x")
            else:
                terminos.append(f"{coef:.3f}x")
        else:
            if coef >= 0 and terminos:
                terminos.append(f" + {coef:.3f}x^{i}")
            else:
                terminos.append(f"{coef:.3f}x^{i}")

print("P(x) =", "".join(terminos))

# 5. Crear la gráfica profesional
plt.figure(figsize=(12, 8))

# Generar puntos para graficar
x_vals = np.linspace(x_min, x_max, 500)
y_vals = [P_n(X, Y, x) for x in x_vals]
y_real = np.tan(x_vals)

# Función real tan(x)
plt.plot(x_vals, y_real, color='red', linewidth=1.5,
         label='tan(x)', linestyle='--', alpha=0.8)

# Curva del polinomio interpolante de Lagrange
plt.plot(x_vals, y_vals, color='blue', linewidth=2,
         label=f'Polinomio de Lagrange de grado {len(X)-1}',
         linestyle='-')

# Puntos de interpolación
plt.scatter(X, Y, color='green', s=80, zorder=5,
           label='Puntos de interpolación', edgecolors='black')

# Anotar coordenadas en cada punto
for i, (x, y) in enumerate(zip(X, Y)):
    plt.annotate(f'({x:.2f}, {y:.2f})', (x, y),
                 xytext=(5, 5), textcoords='offset points',
                 fontsize=8, ha='left',
                 bbox=dict(boxstyle='round,pad=0.15', 
                          fc='white', alpha=0.7),
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

# Líneas de asíntotas en ±π/2
plt.axvline(x=-np.pi/2, color='gray', linestyle=':', alpha=0.5,
           label='Asíntotas de tan(x)')
plt.axvline(x=np.pi/2, color='gray', linestyle=':', alpha=0.5)

# Configuración de la gráfica
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación de Lagrange para f(x) = tan(x)', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)

# Etiquetas del eje x con π
x_ticks = [-np.pi/2, -np.pi/4, 0, np.pi/4, np.pi/2]
x_labels = ['-π/2', '-π/4', '0', 'π/4', 'π/2']
plt.xticks(x_ticks, x_labels)

# Limitar eje Y para evitar valores extremos
plt.ylim(-10, 10)

plt.tight_layout()
plt.savefig('lagrange_mejorado.png', dpi=300, bbox_inches='tight')
print("\nGráfica guardada como 'lagrange_mejorado.png'")

