import numpy as np


def f(x, y):
    """Función a integrar: f(x,y) = y*sin(x)"""
    return y * np.sin(x)


def simpson_doble(c, d, a, b, n, m):
    """
    Método de Simpson para integral doble
    Integra f(x,y) sobre [a,b]×[c,d]
    """
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


if __name__ == "__main__":
    print("Seleccione una de las siguientes opciones:")
    print("1. Aproximar el área bajo la función y*sin(x) donde x va de 0 a pi y y va de 0 a x")
    print("2. Calcular el área de la región donde x va de 0 a 1 y y va de raíz de x a 1")
    print("3. Calcular el área de la región donde x va de 1 a 2 y y va de x a x al cuadrado")
    print("4. Calcular el área de la región donde y va de 0 a 2 y x va de 1 a e elevado a la y")
    print("5. Aproximar el área bajo la función y*sin(x) donde y va de 0 a pi y x va de 0 a 3")
    opcion = int(input("Ingrese el número de la opción: "))

    n = 6  # subintervalos en x (par)
    m = 8  # subintervalos en y (par)

    if opcion == 1:
        # Para límites variables necesitaríamos una implementación diferente
        print("Esta opción requiere límites variables - no implementado")
    elif opcion == 2:
        print("Esta opción requiere límites variables - no implementado")
    elif opcion == 3:
        print("Esta opción requiere límites variables - no implementado")
    elif opcion == 4:
        print("Esta opción requiere límites variables - no implementado")
    elif opcion == 5:
        # Parámetros de integración para la opción 5
        a = 0
        b = 3
        c = 0
        d = np.pi
        resultado = simpson_doble(c, d, a, b, n, m)
        print(f"Resultado de la integral doble: {resultado}")
    else:
        print("Opción no válida")
        exit()
