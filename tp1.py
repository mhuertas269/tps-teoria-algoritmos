import sys


def cargar_monedas(ruta_archivo):
    with open(ruta_archivo, "r") as f:
        for linea in f:
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue
            return [int(x) for x in linea.split(";") if x.strip()]
    return []


def elegir_moneda(fila, inicio, fin, turno_sofia):
    if turno_sofia:
        return "Primera" if fila[inicio] >= fila[fin] else "Última"
    else:
        return "Primera" if fila[inicio] <= fila[fin] else "Última"


def jugar(fila):
    inicio = 0
    fin = len(fila) - 1
    valor_sofia = 0
    valor_mateo = 0
    turno_sofia = True
    jugadas = []

    while inicio <= fin:
        jugador = "Sophia" if turno_sofia else "Mateo"
        eleccion = elegir_moneda(fila, inicio, fin, turno_sofia)

        if eleccion == "Primera":
            moneda = fila[inicio]
            inicio += 1
        else:
            moneda = fila[fin]
            fin -= 1

        if turno_sofia:
            valor_sofia += moneda
        else:
            valor_mateo += moneda

        jugadas.append(f"{eleccion} moneda para {jugador}")
        turno_sofia = not turno_sofia

    return jugadas, valor_sofia, valor_mateo


def imprimir_resultado(movimientos, ganancia_s, ganancia_m):
    print(movimientos)
    print(f"Ganancia de Sophia: {ganancia_s}")
    print(f"Ganancia de Mateo: {ganancia_m}")


def main():
    if len(sys.argv) < 2:
        print("Uso: python3 tp1.py <ruta/a/entrada.txt>")
        return

    ruta_archivo = sys.argv[1]
    fila_monedas = cargar_monedas(ruta_archivo)

    if not fila_monedas:
        print(f"Error: No se pudieron cargar monedas desde '{ruta_archivo}'.")
        return

    movimientos, ganancia_sofia, ganancia_mateo = jugar(fila_monedas)
    imprimir_resultado(movimientos, ganancia_sofia, ganancia_mateo)


if __name__ == "__main__":
    main()
