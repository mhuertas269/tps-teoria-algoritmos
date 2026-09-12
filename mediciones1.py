import time
import numpy as np
from tp1 import jugar
import random
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def medir_tiempo(n, repeticiones=10):
    tiempos = []

    for _ in range(repeticiones):
        fila = [random.randint(1, 1000) for _ in range(n)]

        inicio = time.perf_counter()
        jugar(fila)
        fin = time.perf_counter()

        tiempos.append(fin - inicio)

    return sum(tiempos) / len(tiempos)


def funcion_lineal(n, c1, c2):
    return c1 * n + c2


tamaños = [
    1000,
    5000,
    10000,
    15000,
    20000,
    25000,
    30000,
    35000,
    40000,
    45000,
    50000,
    60000,
    70000,
    80000,
    90000,
    100000,
]

tiempos = []

for n in tamaños:
    tiempo = medir_tiempo(n)
    tiempos.append(tiempo)
    print(n, tiempo)

# Ajuste por cuadrados mínimos

parametros, _ = curve_fit(funcion_lineal, tamaños, tiempos)

c1, c2 = parametros

print("c1 =", c1)
print("c2 =", c2)

# Tiempos dados por el ajuste

tiempos_ajustados = funcion_lineal(np.array(tamaños), c1, c2)

# Error cuadrático total

error_cuadratico = np.sum((tiempos_ajustados - np.array(tiempos)) ** 2)

print("Error cuadrático total:", error_cuadratico)


# Gráfico de mediciones y ajuste

plt.plot(tamaños, tiempos, marker="o", label="Mediciones")
plt.plot(tamaños, tiempos_ajustados, label="Ajuste lineal")

plt.xlabel("Cantidad de monedas (n)")
plt.ylabel("Tiempo (segundos)")
plt.title("Tiempo de ejecución de jugar(n)")
plt.grid()
plt.legend()

plt.savefig("mediciones_ajuste.png")

# Gráfico del error

errores = np.abs(tiempos_ajustados - np.array(tiempos))

plt.figure()

plt.plot(tamaños, errores)

plt.xlabel("Cantidad de monedas (n)")
plt.ylabel("Error absoluto (s)")
plt.title("Error de ajuste")
plt.grid()

plt.savefig("error_ajuste.png")
