#!/usr/bin/env python3
import numpy as np

def gaussxw(N):
    """Calcula los puntos y pesos de Gauss-Legendre en el intervalo [-1, 1].

    Args:
        N (int): Número de puntos (orden del polinomio de Legendre).

    Returns:
        tuple: 
            - x (ndarray): Puntos de muestreo.
            - w (ndarray): Pesos correspondientes.

    Examples:
        >>> x, w = gaussxw(8)
        >>> len(x)
        8
    """
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w

def gaussxwab(a, b, x, w):
    """Escala los puntos y pesos de Gauss-Legendre al intervalo [a, b].

    Args:
        a (float): Límite inferior del intervalo.
        b (float): Límite superior del intervalo.
        x (ndarray): Puntos en el intervalo [-1, 1].
        w (ndarray): Pesos asociados a los puntos en [-1, 1].

    Returns:
        tuple:
            - x_scaled (ndarray): Puntos escalados al intervalo [a, b].
            - w_scaled (ndarray): Pesos escalados al intervalo [a, b].

    Examples:
        >>> x, w = gaussxw(4)
        >>> x_scaled, w_scaled = gaussxwab(0, np.pi, x, w)
    """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

def integralAproximada(argumento):
    """
    Calcula el valor de la función seno de x², es decir, \( \sin(x^2) \).

    Args:
        argumento (float): El valor de x en el que calcular \( \sin(x^2) \).

    Returns:
        float: El valor de \( \sin(x^2) \) para el valor dado de x.

    Examples:
        >>> integralAproximada(0)
        0.0
        >>> integralAproximada(np.pi / 4)
        0.7071067811865475
        >>> integralAproximada(np.pi)
        -0.4303012170000917
    """
    return np.sin(argumento * argumento)


# Se eligen N = 8, 9 y 10 porque la función sin(x²) es altamente oscilatoria
# y requiere mayor precisión al aumentar x.

# Puntos y pesos para N = 8, 9 y 10
xN8, wN8 = gaussxw(8)
xN9, wN9 = gaussxw(9)
xN10, wN10 = gaussxw(10)

# Ahora escalamos los puntos de muestreo y pesos al intervalo [o, π]
puntoMuestreoxN8, pesoMuestreowN8 = gaussxwab(0, np.pi, xN8, wN8)
puntoMuestreoxN9, pesoMuestreowN9 = gaussxwab(0, np.pi, xN9, wN9)

puntoMuestreoxN10, pesoMuestreowN10 = gaussxwab(0, np.pi, xN10, wN10)

"""
Imprimimos en la pantalla el resultado de la suma de la multiplicación del peso por el valor de la integral
en los puntos de muestreo dados; N = 8, 9, 10
"""
print(f"La aproximación de la integral con N=8 es {np.sum(pesoMuestreowN8 * integralAproximada(puntoMuestreoxN8)):.6f}")
print(f"La aproximación de la integral con N=9 es {np.sum(pesoMuestreowN9 * integralAproximada(puntoMuestreoxN9)):.6f}")
print(f"La aproximación de la integral con N=10 es {np.sum(pesoMuestreowN10 * integralAproximada(puntoMuestreoxN10)):.6f}")

