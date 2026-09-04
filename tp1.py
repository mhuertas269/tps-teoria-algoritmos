import random


def inicializar_juego(n, valor_min=1, valor_max=10):
    monedas = [random.randint(valor_min, valor_max) for _ in range(n)]
    return monedas


def elegir_y_remover_moneda(fila, turno_sofia):
    if len(fila) == 1:
        return fila.pop()

    if turno_sofia:
        if fila[0] >= fila[-1]:
            return fila.pop(0)
        else:
            return fila.pop()
    else:
        if fila[0] <= fila[-1]:
            return fila.pop(0)
        else:
            return fila.pop()


def jugar(cant_monedas):
    fila = inicializar_juego(cant_monedas)
    valor_sofia = 0
    valor_mateo = 0
    turno_sofia = True

    while len(fila) > 0:
        moneda = elegir_y_remover_moneda(fila, turno_sofia)

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
