1) Planteamos una solución

En un juego tradicional, en el que cada jugador decide qué moneda tomar en su turno, Sophia no podría determinar de antemano las elecciones de Mateo y para garantizar su victoria debería considerar las posibles decisiones de su oponente y las diferentes secuencias de elecciones que podrían producirse. Sin embargo, en este problema Sophia controla las elecciones de ambos jugadores, lo que le permite utilizar una estrategia greedy basada únicamente en los valores de las monedas disponibles en los extremos.

La estrategia consiste en que, cuando llega el turno de Sophia, elige para sí misma la moneda de mayor valor entre las dos disponibles en los extremos. Cuando llega el turno de Mateo, Sophia elige para él la moneda de menor valor entre los dos extremos disponibles.

Esta estrategia tiene una propiedad fundamental: en cada ronda, la moneda que recibe Mateo tiene un valor menor o igual que la moneda que recibió Sophia inmediatamente antes.

Para demostrarlo, supongamos que al comienzo de una ronda la fila es:
[a,b,c,d]
Sophia puede elegir entre a y d. Supongamos que:
d >= a 
Sophia elige d. Luego, la fila queda:
[a,b,c]
Mateo puede elegir entre a y c, pero Sophia controla su elección y le asigna la moneda de menor valor, o lo que es igual: min(a,c)
Como: min(a,c) <= a <= d se cumple que la moneda recibida por Mateo tiene un valor menor o igual que la moneda que recibió Sophia en esa ronda.

Este mismo razonamiento se aplica en cada ronda del juego. Por lo tanto, si agrupamos las elecciones de Sophia y Mateo de a pares, se cumple: moneda de Mateo <= moneda de Sophia en cada par de turnos. Al sumar estas desigualdades para todas las rondas, obtenemos: valor total de Mateo <= valor total de Sophia

Por lo tanto, la estrategia garantiza que Sophia nunca obtiene un puntaje menor que Mateo.

Puede existir un empate cuando, en todas las rondas, la moneda asignada a Mateo tiene el mismo valor que la moneda elegida por Sophia. Sin embargo, el enunciado indica que se desestime el caso particular en el que hay una cantidad par de monedas de igual valor, ya que en esa situación ambos jugadores reciben la misma cantidad de monedas del mismo valor y el empate se produce independientemente de la estrategia utilizada.

Descartando dicho caso, la estrategia greedy garantiza que Sophia obtiene un puntaje estrictamente mayor que Mateo y, por lo tanto, siempre gana.

6) Corroboración empírica de la complejidad

A partir del análisis teórico se determinó que la complejidad temporal del algoritmo es O(n). Para corroborar experimentalmente este resultado, se realizaron mediciones del tiempo de ejecución para distintos tamaños de entrada, utilizando entre 1.000 y 100.000 monedas. Para cada tamaño se realizaron 10 ejecuciones y se utilizó el tiempo promedio obtenido. Los valores de las monedas fueron generados aleatoriamente entre 1 y 10.

Dado que el análisis teórico indica un comportamiento lineal, se utilizó el modelo T(n)=c1n+c2 y se obtuvo mediante el método de cuadrados mínimos la recta que mejor se ajusta a las mediciones.

En la ejecución realizada se obtuvieron los parámetros:
c1 = 3.223812654606917e-07
c2 = 0.0005992163652310811
dando como resultado el siguiente ajuste: 
T(n)=3.223812654606917e-07n - 0.0004533503429140495

[Gráfico: mediciones-ajuste.png]

Como puede observarse en el gráfico, los tiempos medidos presentan un comportamiento aproximadamente lineal y se encuentran próximos a la recta obtenida mediante el ajuste.

También se calculó el error cuadrático total del ajuste, cuyo valor fue \(1.30\times10^{-5}\). El gráfico de error absoluto muestra la diferencia entre cada tiempo medido y el tiempo estimado por el modelo lineal. Las diferencias observadas son pequeñas en comparación con el crecimiento general de los tiempos, aunque existen algunas mediciones con un error mayor.

[Gráfico: error-cuadrático.png]

En conclusión, el comportamiento observado experimentalmente resulta consistente con la complejidad temporal teórica O(n).
