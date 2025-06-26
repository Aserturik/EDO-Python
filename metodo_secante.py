import numpy as np


def f(x):
    """Función a evaluar: 4*x**2-1-2*x"""
    return 4*x**2-1-2*x


# Parámetros de entrada
x0, x1 = 1, 2
eps1, eps2 = 0.001, 0.001
k = 0
max_iter = 20

# Verificar que los puntos iniciales son diferentes
if np.abs(x1 - x0) < 1e-15:
    print(f"Error: los puntos iniciales son iguales x0 = {x0}, x1 = {x1}")
    exit()

# Calcular valores iniciales de la función
f0 = f(x0)
f1 = f(x1)

# Verificar división por cero antes del primer cálculo
if np.abs(f1 - f0) < 1e-15:
    print("Error: f(x1) - f(x0) = 0, no se puede iniciar el método")
    print(f"f({x0}) = {f0}, f({x1}) = {f1}")
    exit()

# Calcular la primera aproximación
x2 = x1 - f1 * (x1 - x0) / (f1 - f0)

# Imprimir encabezados de la tabla
print("=" * 80)
print(f"{'Iter':<6} {'x0':<12} {'x1':<12} {
      'x2':<12} {'|x2-x1|':<12} {'|f(x2)|':<12}")
print("=" * 80)

while np.abs(x2 - x1) > eps1 and np.abs(f(x2)) > eps2 and k < max_iter:
    f2 = f(x2)
    print(f"{k:<6} {x0:<12.8f} {x1:<12.8f} {x2:<12.8f} "
          f"{np.abs(x2 - x1):<12.8f} {np.abs(f2):<12.8f}")
    k += 1
    # Actualizar puntos para la siguiente iteración
    x0 = x1
    x1 = x2
    f0 = f1
    f1 = f2
    # Verificar división por cero
    if np.abs(f1 - f0) < 1e-15:
        print(
            f"Error: f(x1) - f(x0) = 0 en la iteración {k}, no se puede continuar")
        print(f"f({x0}) = {f0}, f({x1}) = {f1}")
        break
    # Calcular siguiente aproximación
    x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
print("=" * 80)

# Verificar convergencia y mostrar resultados
if k >= max_iter:
    print(f'No convergió después de {max_iter} iteraciones')
    print(f'Última aproximación: x = {x2:.10f}')
    print(f'Error absoluto: |x2-x1| = {np.abs(x2-x1):.2e}')
    print(f'Valor de la función: f(x2) = {f(x2):.2e}')
else:
    print(f'La solución es: x = {x2:.10f}')
    print(f'Convergencia alcanzada en {k} iteraciones')
    print(f'Error absoluto final: |x2-x1| = {np.abs(x2-x1):.2e}')
    print(f'Verificación: f(x) = {f(x2):.2e}')
