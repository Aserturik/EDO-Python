import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Función de la ecuación diferencial

def f(x, y):
    return -x/y 

x_min = -2
x_max = 2
num_points = 17
x = np.linspace(x_min, x_max, num_points)
y = np.linspace(x_min, x_max, num_points)
X, Y = np.meshgrid(x, y)

fig, ax = plt.subplots()
Q = ax.quiver(X, Y, np.ones_like(X), f(X, Y))

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Campo Direccional de la Ecuación Diferencial')
ax.grid()

fig, ax = plt.subplots()
Q = ax.quiver(X, Y, np.ones_like(X), f(X, Y))

# Agregar curvas de nivel de la función
levels = np.linspace(-3, 3, 30)
contour = ax.contourf(X, Y, f(X, Y), levels=levels, cmap='coolwarm', alpha=0.5)

def update_quiver(num, Q, X, Y):
    # Calcula los nuevos datos de la función
    t = num / 100
    x = np.linspace(x_min, x_max, num_points)
    y = np.linspace(x_min + t, x_max + t, num_points)
    X, Y = np.meshgrid(x, y)
    dx_dy = f(X, Y)  # Corregido aquí
    # Actualiza los datos del gráfico
    Q.set_UVC(np.ones_like(dx_dy), dx_dy)
    Q.set_offsets(np.column_stack([X.ravel(), Y.ravel()]))
    return Q,


ani = animation.FuncAnimation(fig, update_quiver, fargs=(Q, X, Y), frames=100, interval=50, blit=True)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from moviepy.editor import *

# Resto del código para definir la animación...

# Crear la animación
ani = animation.FuncAnimation(fig, update_quiver, fargs=(Q, X, Y), frames=100, interval=50, blit=True)

# Mostrar la animación
plt.show()
