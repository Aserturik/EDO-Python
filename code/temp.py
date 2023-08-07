import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def f(x, y):
    return x**2 + y**2 - 1

x_min = -2
x_max = 2
num_points = 15
x = np.linspace(x_min, x_max, num_points)
y = np.linspace(x_min, x_max, num_points)
X, Y = np.meshgrid(x, y)

def update_quiver(num, Q, X, Y):
    dx_dy = f(X, Y)
    Q.set_UVC(np.ones_like(dx_dy), dx_dy)
    return Q,

fig, ax = plt.subplots()
Q = ax.quiver(X, Y, np.ones_like(X), f(X, Y))

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Campo Direccional de la Ecuación Diferencial')
ax.grid()

ani = animation.FuncAnimation(fig, update_quiver, fargs=(Q, X, Y), frames=100, interval=50, blit=True)

plt.show()
