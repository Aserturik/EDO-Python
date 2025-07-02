import numpy as np

x1 = np.array([1, 1, 0], dtype=float)
x2 = np.array([0, 1, 0], dtype=float)
x3 = np.array([1, 1, 1], dtype=float)

# A = np.array([0, 5, 5, 0], [0, 1, 1, 0], [1, 1, 1, 1], dtype=float)

print('Vectores originales LI:')
print(x1, x2, x3)

e1 = x1.copy()
alfa12 = np.dot(x2, e1) / np.dot(e1, e1)
e2 = x2 - alfa12 * e1

alfa13 = np.dot(x3, e1) / np.dot(e1, e1)
alfa23 = np.dot(x3, e2) / np.dot(e2, e2)
e3 = x3 - (alfa13 * e1) - alfa23 * e2

print('\nVectores ortogonales:')
print(e1, e2, e3)

print(f'e1*e2 = {np.dot(e1, e2)}')
print(f'e1*e3 = {np.dot(e1, e3)}')
print(f'e2*e3 = {np.dot(e2, e3)}')


#
#
#
# import numpy as np
#
# x1 = np.array([1, 1, 0], dtype=float)
# x2 = np.array([0, 1, 0], dtype=float)
# x3 = np.array([1, 1, 1], dtype=float)
#
# print('Vectores originales LI:')
# print(x1, x2, x3)
#
# e1 = x1.copy()
# alfa12 = np.dot(x2, e1) / np.dot(e1, e1)
# e2 = x2 - alfa12 * e1
#
# alfa13 = np.dot(x3, e1) / np.dot(e1, e1)
# alfa23 = np.dot(x3, e2) / np.dot(e2, e2)
# e3 = x3 - (alfa13 * e1) - alfa23 * e2
#
# print('\nVectores ortogonales:')
# print(e1, e2, e3)
#
# print(f'e1*e2 = {np.dot(e1, e2)}')
# print(f'e1*e3 = {np.dot(e1, e3)}')
# print(f'e2*e3 = {np.dot(e2, e3)}')
#
#
