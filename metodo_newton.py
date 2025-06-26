import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Usar backend no interactivo antes de importar pyplot


def f(x):
    return 2*x**2 - x - 5


def df(x):
    return 4*x - 1


x0, eps1, eps2, k = 2, 0.0001, 0.0001, 0
max_iter = 100

# Verificar división por cero antes del primer cálculo
if np.abs(df(x0)) < 1e-15:
    print(f"Error: la derivada es cero en x0 = {x0}, "
          f"no se puede iniciar el método")
    exit()

x1 = x0 - (f(x0)/df(x0))

# Imprimir encabezados de la tabla
print("=" * 70)
print(f"{'Iter':<6} {'x0':<12} {'x1':<12} {'|x1-x0|':<12} {'|f(x1)|':<12}")
print("=" * 70)

while np.abs(x1-x0) > eps1 and np.abs(f(x1)) > eps2 and k < max_iter:
    print(f"{k:<6} {x0:<12.8f} {x1:<12.8f} {np.abs(x1-x0):<12.8f} "
          f"{np.abs(f(x1)):<12.8f}")
    k = k+1
    x0 = x1
    if np.abs(df(x0)) < 1e-15:
        print(f"Error: la derivada es cero en x = {x0}, no se puede continuar")
        break
    x1 = x0 - (f(x0)/df(x0))
print("=" * 70)

if k >= max_iter:
    print(f'No convergió después de {max_iter} iteraciones')
else:
    print(f'La solución es: x = {x1:.10f}')
    print(f'Verificación: f(x) = {f(x1):.2e}')


x = np.linspace(-2, 2.5, 100)
y = f(x)
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='red', label='f(x) = 4x² - 2x - 5')
plt.plot(x, 0*x, color='black', linestyle='--', label='y = 0')
plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='black', linestyle='-', alpha=0.3)
plt.plot(x1, f(x1), 'go', markersize=8, label=f'Raíz: x = {x1:.6f}')
plt.plot(x1, f(-2), 'go', markersize=8, label=f'Raíz: x = {x1:.6f}')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método de Newton-Raphson')
plt.legend()
plt.savefig('metodo_newton_grafica.png', dpi=300, bbox_inches='tight')
print('Gráfica guardada como: metodo_newton_grafica.png')
