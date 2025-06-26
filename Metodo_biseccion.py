# Método de bisección

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Usar backend no interactivo antes de importar pyplot


def f(x):
    return 2*x**2 - x - 5


def biseccion(xi, xd, eps1=0.0001, eps2=0.0001, max_iter=100,
              mostrar_tabla=True):
    """
    Implementa el método de bisección para encontrar una raíz

    Args:
        xi: límite izquierdo del intervalo
        xd: límite derecho del intervalo
        eps1: tolerancia para el cambio en la raíz
        eps2: tolerancia para |f(xm)|
        max_iter: máximo número de iteraciones
        mostrar_tabla: si mostrar la tabla de iteraciones

    Returns:
        tuple: (raíz encontrada, número de iteraciones, convergió)
    """
    k = 0

    # Asegurar que xi < xd
    if xi > xd:
        xi, xd = xd, xi

    # Calcular valores de la función en los extremos
    f_xi = f(xi)
    f_xd = f(xd)

    # Verificar que f(xi) y f(xd) tienen signos opuestos
    if f_xi * f_xd >= 0:
        print(f"Error: f({xi}) * f({xd}) = {f_xi * f_xd:.6f} >= 0, "
              "los puntos no están al lado de una raíz.")
        return None, 0, False

    # Verificar si algún extremo ya es la raíz
    if np.abs(f_xi) <= eps2:
        if mostrar_tabla:
            print(f"El punto xi = {xi} ya es una raíz con f(xi) = {f_xi:.2e}")
        return xi, 0, True

    if np.abs(f_xd) <= eps2:
        if mostrar_tabla:
            print(f"El punto xd = {xd} ya es una raíz con f(xd) = {f_xd:.2e}")
        return xd, 0, True

    if mostrar_tabla:
        print("=" * 80)
        print(f"{'Iter':<6} {'xi':<12} {'xd':<12} {'xm':<12} "
              f"{'|xm-xm_ant|':<12} {'|f(xm)|':<12}")
        print("=" * 80)

    xm_anterior = None

    while k < max_iter:
        # Calcular punto medio usando la fórmula de bisección
        xm = (xi + xd) / 2
        f_xm = f(xm)

        # Calcular error si no es la primera iteración
        error_xm = np.abs(
            xm - xm_anterior) if xm_anterior is not None else float('inf')

        if mostrar_tabla:
            print(f"{k:<6} {xi:<12.8f} {xd:<12.8f} {xm:<12.8f} "
                  f"{error_xm:<12.8f} {np.abs(f_xm):<12.8f}")

        # Verificar criterios de convergencia
        convergencia_valor = np.abs(f_xm) <= eps2
        convergencia_cambio = xm_anterior is not None and error_xm <= eps1
        ancho_intervalo = xd - xi
        convergencia_intervalo = ancho_intervalo <= 2 * eps1

        # Convergencia si se cumple el criterio de función Y otro criterio
        if convergencia_valor and (convergencia_cambio or convergencia_intervalo):
            if mostrar_tabla:
                print("=" * 80)
            return xm, k, True

        # Verificar si el intervalo es demasiado pequeño
        if ancho_intervalo < np.finfo(float).eps * max(abs(xi), abs(xd)):
            if mostrar_tabla:
                print("=" * 80)
                print("Intervalo alcanzó la precisión de la máquina")
            return xm, k, True

        # Actualizar el intervalo según el teorema del valor intermedio
        if f_xi * f_xm > 0:
            xi = xm  # La raíz está entre xm y xd
            f_xi = f_xm
        else:
            xd = xm  # La raíz está entre xi y xm
            f_xd = f_xm

        # Preparar para la siguiente iteración
        k += 1
        xm_anterior = xm

    # Si no converge en max_iter iteraciones
    if mostrar_tabla:
        print("=" * 80)
        print(f'No convergió después de {max_iter} iteraciones')

    return None, k, False


# Código principal para ejecutar el método
if __name__ == "__main__":
    # Definir intervalos para encontrar diferentes raíces
    intervalos = [(-3, 0), (1, 3)]
    raices_encontradas = []

    print("BÚSQUEDA DE RAÍCES CON EL MÉTODO DE BISECCIÓN")
    print("=" * 80)

    for i, (xi, xd) in enumerate(intervalos):
        print(f"\nINTERVALO {i+1}: [{xi}, {xd}]")
        print("-" * 50)

        raiz, iteraciones, convergio = biseccion(xi, xd, mostrar_tabla=True)

        if convergio:
            print(f'La solución es: x = {raiz:.10f}')
            print(f'Verificación: f(x) = {f(raiz):.2e}')
            print(f'Iteraciones: {iteraciones}')

            # Verificar si esta raíz ya fue encontrada (evitar duplicados)
            es_nueva = True
            for raiz_existente in raices_encontradas:
                if np.abs(raiz - raiz_existente) < 1e-6:
                    es_nueva = False
                    break

            if es_nueva:
                raices_encontradas.append(raiz)
                print("*** NUEVA RAÍZ ENCONTRADA ***")
            else:
                print("(Raíz ya encontrada anteriormente)")
        else:
            print(f"No convergió después de {iteraciones} iteraciones")

    print(f"\n" + "=" * 80)
    print("RESUMEN DE RAÍCES ENCONTRADAS:")
    print("=" * 80)
    for i, raiz in enumerate(raices_encontradas):
        print(f"Raíz {i+1}: x = {raiz:.10f}, f(x) = {f(raiz):.2e}")

    # Generar la gráfica con todas las raíces encontradas
    x = np.linspace(-3, 4, 400)
    y = f(x)
    plt.figure(figsize=(12, 8))
    plt.plot(x, y, color='blue', linewidth=2, label='f(x) = 2x² - x - 5')
    plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='black', linestyle='-', alpha=0.3)

    # Plotear todas las raíces encontradas
    colores = ['red', 'green', 'orange', 'purple', 'brown']
    for i, raiz in enumerate(raices_encontradas):
        color = colores[i % len(colores)]
        plt.plot(raiz, f(raiz), 'o', markersize=10, color=color,
                 label=f'Raíz {i+1}: x = {raiz:.6f}')
        plt.axvline(x=raiz, color=color, linestyle='--', alpha=0.5)

    # Mostrar los intervalos usados en la gráfica
    for i, (xi, xd) in enumerate(intervalos):
        plt.axvspan(xi, xd, alpha=0.1, color='gray',
                    label=f'Intervalo {i+1}: [{xi}, {xd}]' if i < 2 else "")

    plt.grid(True, alpha=0.3)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('f(x)', fontsize=12)
    plt.title('Método de Bisección - Múltiples Raíces', fontsize=14)
    plt.legend()

    # Agregar texto con información
    textstr = f'Raíces encontradas: {len(raices_encontradas)}\n'
    textstr += f'Intervalos probados: {len(intervalos)}'
    props = dict(boxstyle='round', facecolor='lightblue', alpha=0.5)
    plt.text(0.02, 0.98, textstr, transform=plt.gca().transAxes, fontsize=10,
             verticalalignment='top', bbox=props)

    plt.tight_layout()
    plt.savefig('biseccion_grafica.png', dpi=300, bbox_inches='tight')
    print('\nGráfica guardada como: biseccion_grafica.png')
    print(f'La gráfica muestra {len(raices_encontradas)} raíces encontradas '
          f'usando {len(intervalos)} intervalos')
