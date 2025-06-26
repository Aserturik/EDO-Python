import numpy as np


def f(x):
    return 4*x**2-1-2*x


def df(x):
    return 8*x - 2


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
