import matplotlib.pyplot as plt
import numpy as np

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Datos para el gráfico
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Agregar un gráfico de líneas a los ejes
ax.plot(x, y, label='Seno(x)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Gráfico de Seno')
ax.legend()

# Mostrar el gráfico
plt.show()

