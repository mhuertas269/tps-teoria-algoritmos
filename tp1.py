import random


def inicializar_juego(n, valor_min=1, valor_max=10):
    monedas = [random.randint(valor_min, valor_max) for _ in range(n)]
    return monedas


def elegir_moneda(fila, inicio, fin, turno_sofia):

    if turno_sofia:
        if fila[inicio] >= fila[fin]:
            return fila[inicio], inicio + 1, fin
        else:
            return fila[fin], inicio, fin - 1
    else:
        if fila[inicio] <= fila[fin]:
            return fila[inicio], inicio + 1, fin
        else:
            return fila[fin], inicio, fin - 1 


def jugar(cant_monedas):
    fila = inicializar_juego(cant_monedas)
    valor_sofia = 0
    valor_mateo = 0
    turno_sofia = True

    inicio = 0
    fin = len(fila) - 1

    while inicio <= fin:
        moneda, inicio, fin = elegir_moneda(fila, inicio, fin, turno_sofia)

        if turno_sofia:
            valor_sofia += moneda
        else:
            valor_mateo += moneda

        turno_sofia = not turno_sofia

    if valor_sofia > valor_mateo:
        return "Gano Sofia"
    elif valor_mateo > valor_sofia:
        return "Gano Mateo"
    else:
        return "Empate"

