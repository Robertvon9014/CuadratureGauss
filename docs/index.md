# Bienvenido al Módulo: Cuadratura Gaussiana

En este proyecto abordamos el problema de calcular integrales definidas de funciones oscilatorias utilizando un método numérico avanzado: la cuadratura de Gauss-Legendre. El objetivo principal es demostrar cómo se puede aplicar este método para obtener aproximaciones precisas de integrales que no pueden resolverse de forma analítica.

La integral que se desea evaluar es:

\begin{align}
\int_{0}^{\pi}\sin(x^2)dx
\end{align}
una función cuya oscilación rápida y la falta de una primitiva elemental hacen que sea un excelente caso de estudio para técnicas de integración numérica.

Para resolver esta integral se utiliza el método de cuadratura de Gauss-Legendre, que consiste en una fórmula de integración de la forma:
\begin{align}
\int_{a}^{b} dxf(x) \approx \sum_{k=1}^{N} w_k f(x_k).
\end{align}

donde $x_i$ y $w_i$ son los **puntos** y **pesos** óptimos seleccionados para maximizar la precisión con el menor número de evaluaciónes posibles.
Este método es particularmente eficiente para funcioes suaves, y en este caso se adapta adecuadamente incluso ante la oscilación de $\sin(x^2)$.

Este método considera varios valores de N: 8, 9 y 10, para analizar cómo varía la precisión del resultado a medida que se incrementa el número de puntos de evaluación.
