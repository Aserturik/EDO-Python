import numpy as np


def simpson_doble(f, c, d, a, b, n, m):
    if n % 2 != 0 or m % 2 != 0:
        raise ValueError("n y m deben ser números pares")

    h1 = (b - a) / n  # Paso en x
    h2 = (d - c) / m  # Paso en y

    # Inicializar suma
    suma = 0

    for i in range(n + 1):
        x = a + i * h1

        # Determinar peso en x
        if i == 0 or i == n:
            peso_x = 1
        elif i % 2 == 1:
            peso_x = 4
        else:
            peso_x = 2

        for j in range(m + 1):
            y = c + j * h2

            # Determinar peso en y
            if j == 0 or j == m:
                peso_y = 1
            elif j % 2 == 1:
                peso_y = 4
            else:
                peso_y = 2

            # Peso total = peso_x * peso_y
            peso_total = peso_x * peso_y
            suma += peso_total * f(x, y)

    area = (h1 * h2 / 9) * suma
    return area


def simpson_doble_variable(f, a, b, n, g1, g2, m, direccion='y'):
    # Simpson para límites variables
    # direccion='y': y va de g1(x) a g2(x) (límites variables en y)
    # direccion='x': x va de g1(y) a g2(y) (límites variables en x)
    if n % 2 != 0 or m % 2 != 0:
        raise ValueError("n y m deben ser números pares")

    suma = 0

    if direccion == 'y':
        # Límites variables en y: y va de g1(x) a g2(x)
        h1 = (b - a) / n
        
        for i in range(n + 1):
            x = a + i * h1
            
            # Determinar peso en x
            if i == 0 or i == n:
                peso_x = 1
            elif i % 2 == 1:
                peso_x = 4
            else:
                peso_x = 2
                
            # Límites variables en y
            y_inf = g1(x)
            y_sup = g2(x)
            h2 = (y_sup - y_inf) / m
            
            for j in range(m + 1):
                y = y_inf + j * h2
                
                # Determinar peso en y
                if j == 0 or j == m:
                    peso_y = 1
                elif j % 2 == 1:
                    peso_y = 4
                else:
                    peso_y = 2
                    
                peso_total = peso_x * peso_y
                suma += peso_total * f(x, y) * h2 / 3

        area = h1 / 3 * suma
        
    else:  # direccion == 'x'
        # Límites variables en x: x va de g1(y) a g2(y)
        h2 = (b - a) / m
        
        for j in range(m + 1):
            y = a + j * h2
            
            # Determinar peso en y
            if j == 0 or j == m:
                peso_y = 1
            elif j % 2 == 1:
                peso_y = 4
            else:
                peso_y = 2
                
            # Límites variables en x
            x_inf = g1(y)
            x_sup = g2(y)
            h1 = (x_sup - x_inf) / n
            
            for i in range(n + 1):
                x = x_inf + i * h1
                
                # Determinar peso en x
                if i == 0 or i == n:
                    peso_x = 1
                elif i % 2 == 1:
                    peso_x = 4
                else:
                    peso_x = 2
                    
                peso_total = peso_x * peso_y
                suma += peso_total * f(x, y) * h1 / 3

        area = h2 / 3 * suma
    
    return area


if __name__ == "__main__":
    print("Seleccione una de las siguientes opciones:")
    print("1. Integral de y*sen(x) donde x va de 0 a y y y va de 0 a pi")
    print("2. Integral de 1 donde x va de 0 a 1 y y va de raíz de x a 1")
    print("3. Integral de 1 donde x va de 1 a 2 y y va de x a x al cuadrado")
    print("4. Integral de 1 donde y va de 0 a 2 y x va de 1 a e elevado a la y")
    print("5. Integral de la y*sen(x) donde y va de 0 a pi y x va de 0 a 3")
    opcion = int(input("Ingrese el número de la opción: "))

    n = 6  # subintervalos en x
    m = 8  # subintervalos en y

    if opcion < 1 or opcion > 5:
        print("Opción no válida")
        exit()

    if opcion == 1:
        def f1(x, y): return y * np.sin(x)
        resultado = simpson_doble_variable(
            f1, 0, np.pi, m, lambda y: 0, lambda y: y, n, direccion='x')
    elif opcion == 2:
        def f2(x, y): return 1
        resultado = simpson_doble_variable(
            f2, 0, 1, n, lambda x: np.sqrt(x), lambda x: 1, m)
    elif opcion == 3:
        def f3(x, y): return 1
        resultado = simpson_doble_variable(
            f3, 1, 2, n, lambda x: x, lambda x: x**2, m)
    elif opcion == 4:
        def f4(x, y): return 1
        resultado = simpson_doble_variable(f4, 1, np.exp(
            2), n, lambda x: np.log(x), lambda x: 2, m)
    else:  # opcion == 5
        def f5(x, y): return y * np.sin(x)
        a = 0
        b = 3
        c = 0
        d = np.pi
        resultado = simpson_doble(f5, c, d, a, b, n, m)

    print(f"Resultado de la integral doble: {resultado}")
