import numpy as np


def gauss_seidel(A, B, X0, tolerance, max_iterations=100):
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)
    X0 = np.array(X0, dtype=float)
    matrix_shape = np.shape(A)
    n = matrix_shape[0]
    m = matrix_shape[1]

    iteration = 0
    X = np.copy(X0)
    X_prev = np.copy(X0)

    while iteration < max_iterations:
        X_prev = np.copy(X)

        for i in range(n):
            sum_value = B[i]
            for j in range(m):
                if i != j:
                    sum_value = sum_value - A[i, j] * X[j]
            X[i] = sum_value / A[i, i]

        # Criterio de convergencia relativo mejorado
        relative_error = np.linalg.norm(
            X - X_prev) / (np.linalg.norm(X) + 1e-16)

        iteration += 1

        if relative_error < tolerance:
            break

    # No converge
    if iteration >= max_iterations:
        print('Advertencia: No converge, máximo de iteraciones alcanzado')
        return None, iteration

    return X, iteration


def partial_pivot_rows(A, B, show_table=False):
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)
    # Matriz aumentada
    B_dimensions = len(np.shape(B))
    if B_dimensions == 1:
        B = np.transpose([B])
    augmented_matrix = np.concatenate((A, B), axis=1)

    if show_table:
        print('Matriz aumentada')
        print(augmented_matrix)
        print('Pivoteo parcial:')

    # Pivoteo por filas AB
    matrix_shape = np.shape(augmented_matrix)
    n = matrix_shape[0]

    # Para cada fila en AB
    pivot_count = 0
    for col in range(n - 1):
        # columna desde diagonal i en adelante
        column = np.abs(augmented_matrix[col:, col])
        max_index = np.argmax(column)

        # max_index no es en diagonal
        if max_index != 0:
            # intercambia filas
            temp_row = np.copy(augmented_matrix[col, :])
            augmented_matrix[col, :] = augmented_matrix[max_index + col, :]
            augmented_matrix[max_index + col, :] = temp_row

            pivot_count += 1
            if show_table:
                print(' ', pivot_count, 'intercambiar filas: ', col, 'y',
                      max_index + col)
    if show_table:
        if pivot_count == 0:
            print('  Pivoteo por filas NO requerido')
        else:
            print('AB')
    return augmented_matrix


A = [[-1, 3, 5, 2],
     [1, 9, 8, 4],
     [0, 1, 0, 1],
     [2, 1, 1, -1]]
B = [10, 15, 2, -3]

X0 = [0, 0, 0, 0]
tolerance = 0.0001
max_iterations = 100

augmented_matrix = partial_pivot_rows(A, B, show_table=True)
n, m = np.shape(augmented_matrix)

A = augmented_matrix[:, :n]  # separa en A y B
B = augmented_matrix[:, n]

gauss_seidel_solucion, num_iterations = gauss_seidel(
    A, B, X0, tolerance, max_iterations)

print('Solucion: ', gauss_seidel_solucion)
