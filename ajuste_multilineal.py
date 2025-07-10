# Aproximación multilineal
import numpy as np
import matplotlib.pyplot as plt

y = np.array([27.5, 28, 28.8, 29.1, 30, 31, 32],
             dtype=float)  # porcentaje de agua
u = np.array([2, 3.5, 4.5, 2.5, 8.5, 10.5, 13.5],
             dtype=float)  # porcentaje de cal
v = np.array([18, 16.5, 10.5, 2.5, 9, 4.5, 1.5],
             dtype=float)  # porcentaje de agua

m = len(y)
Matriz = np.array([[m, np.sum(u), np.sum(v)],
                   [np.sum(u), np.sum(u**2), np.sum(v*u)],
                   [np.sum(v), np.sum(v*u), np.sum(v**2)]],
                  dtype=float)

b = np.array([[np.sum(y)], [np.sum(y*u)], [np.sum(y*v)]], dtype=float)

print('matriz \n', Matriz)
print('vector columna b (Terminos independientes): \n', b)

a = np.linalg.solve(Matriz, b)
print('solucion: \n', a)


def F(a, u_val, v_val):
    return a[0][0]+a[1][0]*u_val+a[2][0]*v_val


per_cal = 10
per_puzolana = 30
y_h2O = F(a, 10, 30)

print(f'si cal = {per_cal}% y puzolana = {
      per_puzolana}%, el del agua es de: {y_h2O}%')

# Crear gráfico de dispersión 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Gráfico de dispersión de los datos originales
ax.scatter(u, v, y, c='blue', marker='o', s=100, alpha=0.8,
           label='Datos originales')

# Crear una malla para la superficie del polinomio
u_range = np.linspace(min(u), max(u), 20)
v_range = np.linspace(min(v), max(v), 20)
U, V = np.meshgrid(u_range, v_range)
Z = a[0][0] + a[1][0]*U + a[2][0]*V

# Superficie del polinomio ajustado
ax.plot_surface(U, V, Z, alpha=0.3, color='red', label='Superficie ajustada')

# Marcar el punto de predicción
ax.scatter([per_cal], [per_puzolana], [y_h2O], c='green', marker='^', s=200,
           label=f'Predicción (Cal={per_cal}%, Puzolana={per_puzolana}%)')

# Etiquetas y título
ax.set_xlabel('Porcentaje de Cal (u)')
ax.set_ylabel('Porcentaje de Puzolana (v)')
ax.set_zlabel('Porcentaje de Agua (y)')
ax.set_title('Aproximación Multilineal: Porcentaje de Agua vs Cal y Puzolana')

# Agregar leyenda
ax.legend()

# Mostrar el gráfico
plt.tight_layout()
plt.savefig('3d.png')
