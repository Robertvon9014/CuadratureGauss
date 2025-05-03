# Explicación

En este apartado trata sobre la **integración numérica**, usando el método de cuadratura Gauss-Legendre, que se aplica al cálculo aproximado de integrales definidas para funciones oscilatorias.

## Integración Numérica

La integración númerica es un método fundamental en matemáticas aplicadas y física computacional. Se usa para aproximar el resultado de una integral definida cuando no es posible obtenerla mediante soluciones analíticas.

Usando el método de la **Cuadratura de Gauss**, la cual selecciona de forma óptima los puntos de muestreo $x_i$ y los pesos $w_i$ para minimizar el error de aproximación.

La forma general de la integral aproximada es:
\begin{align}
\int_a^b {\rm{d}}x f(x) \approx \sum_{k=1}^{N} w_k f(x_k).
\end{align}

* f(x) es la función a integrar.
* $x_i$ son los puntos de muestreo.
* $w_i$ son los pesos asociados a cada punto.

En particular, en la **cuadratura Gaussiana**, los puntos $x_i$ y los pesos $w_i$ están determinados por los ceros de los polinomios de Legendre, y están optimizados para el intervalo [-1, 1].

## Cambio de intervalo
Dado que este método está definido originalmente para el intervalo [-1, 1], es necesario realizar un cambio de variables cuando la integral se evalua sobre un intervalo arbitrario [a, b]. Este cambio se realiza mediante la transformación:
\begin{align}
x_{i}^{'} = \frac{1}{2}(b - a)x_i + \frac{1}{2}(b + a)
\end{align}
\begin{align}
w_{i}^{'} = \frac{1}{2}(b - a)w_i
\end{align}
lo cual ajusta los puntos y pesos para adaptarlos al intervalo deseado.

En este trabajo se evaluó numéricamente la siguiente integral:

\begin{align}
int_{0}^{\pi} sin(x^2)dx
\end{align}
una función **oscilatoria** cuya integral no tiene una forma cerrada.
Se utiliza la función np.polynomial.legendre.leggauss(N) de NumPy, que proporciona los puntos y pesos para un número N de nodos. Luego se aplican los cambios de intervalo para ajustar los puntos al dominio de integración $[0, \pi]$.

Consideramos tres valores de N: 8, 9, 10, con el motivo de observar como mejora la precisión del resultado al aumentar el número de nodos.

La función que se integra es:
```python
def integralAproximada(argumento):
    retunr np.sin(argumento * argumento)

y la integral se evalúa como:
np.sum(pesosMuestreo * integralAproximada(puntosMuestreo))
```

## Reflexiones
Observamos que el método de cuadratura de Gauss-Legendre muestra una eficacia al trabajar con funciones oscilatorias, debido a que estas presentan desafios con métodos muchos más simples, tales como el método del trapezoide o el método de Simpson.
Cuando se aumenta el número de puntos de muestreo N, obtenemos una mejor aproximación del área bajo la curva, esto debido que para número pequeños de N el valor de aproximación oscila alto. 
