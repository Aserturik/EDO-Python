from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Configurar backend para no mostrar gráficas


def f1(x, y):
    """Función f1(x, y) = x² - 10x + y² + 8"""
    return x**2 - 10*x + y**2 + 8


def f2(x, y):
    """Función f2(x, y) = xy² + x - 10y + 8"""
    return x*y**2 + x - 10*y + 8


# Crear grilla de puntos para las gráficas
x = np.linspace(-5, 15, 100)
y = np.linspace(-5, 15, 100)
X, Y = np.meshgrid(x, y)

# Calcular valores de las funciones
Z1 = f1(X, Y)
Z2 = f2(X, Y)

# Crear figura con subplots para las gráficas 3D
fig = plt.figure(figsize=(16, 12))

# Gráfica 3D de f1
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
surf1 = ax1.plot_surface(X, Y, Z1, cmap='viridis', alpha=0.8)
ax1.set_title('Función f1(x, y) = x² - 10x + y² + 8', fontsize=12)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('f1(x, y)')
fig.colorbar(surf1, ax=ax1, shrink=0.5)

# Gráfica 3D de f2
ax2 = fig.add_subplot(2, 2, 2, projection='3d')
surf2 = ax2.plot_surface(X, Y, Z2, cmap='plasma', alpha=0.8)
ax2.set_title('Función f2(x, y) = xy² + x - 10y + 8', fontsize=12)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('f2(x, y)')
fig.colorbar(surf2, ax=ax2, shrink=0.5)

# Gráfica de contorno de f1
ax3 = fig.add_subplot(2, 2, 3)
contour1 = ax3.contour(X, Y, Z1, levels=20, cmap='viridis')
ax3.clabel(contour1, inline=True, fontsize=8)

