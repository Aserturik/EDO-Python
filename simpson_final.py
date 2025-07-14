# Metodo de Simpson 1/3 para integral doble
import numpy as np


def f(x, y):
    # Define the function to integrate
    return y*np.sin(x)  # Example function, modify as needed)


def simpson_1_3(f, a, b, c, d, n, m):
    """
    Perform double integration using Simpson's 1/3 rule.

    Parameters:
    f : function
        The function to integrate.
    a, b : float
        The limits of integration for x.
    c, d : float
        The limits of integration for y.
    n : int
        Number of subintervals for x (must be even).
    m : int
        Number of subintervals for y (must be even).

    Returns:
    float
        The result of the double integral.
    """
    hx = (b - a) / n
    hy = (d - c) / m

    integral = 0

    for i in range(n + 1):
        for j in range(m + 1):
            x = a + i * hx
            y = c + j * hy

            coeff = 1

            if i == 0 or i == n:
                coeff *= 1
            elif i % 2 == 0:
                coeff *= 2
            else:
                coeff *= 4

            if j == 0 or j == m:
                coeff *= 1
            elif j % 2 == 0:
                coeff *= 2
            else:
                coeff *= 4

            integral += coeff * f(x, y)

    integral *= (hx * hy) / 9

    return integral


# Example usage
if __name__ == "__main__":
    a, b = 0, 3  # Limits for x
    c, d = 0, np.pi  # Limits for y
    n, m = 6, 8  # Number of subintervals (must be even)

    result = simpson_1_3(f, a, b, c, d, n, m)
    print("Result of the double integral:", result)
