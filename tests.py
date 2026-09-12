import os
from tp1 import cargar_monedas, jugar

RUTA_DATOS = "archivos-pruebas/"


def tests_catedra():
    def test_20():
        monedas = cargar_monedas(os.path.join(RUTA_DATOS, "20.txt"))
        jugadas, ganancia_s, ganancia_m = jugar(monedas)
        assert ganancia_s > ganancia_m, f"Falló en 20: S={ganancia_s} <= M={ganancia_m}"
        print("Test 20 Monedas: OK")
        print(f"Ganancia de Sophia: {ganancia_s}")
        print(f"Ganancia de Mateo: {ganancia_m}\n")

    def test_25():
        monedas = cargar_monedas(os.path.join(RUTA_DATOS, "25.txt"))
        jugadas, ganancia_s, ganancia_m = jugar(monedas)
        assert ganancia_s > ganancia_m, f"Falló en 25: S={ganancia_s} <= M={ganancia_m}"
        print("Test 25 Monedas: OK")
        print(f"Ganancia de Sophia: {ganancia_s}")
        print(f"Ganancia de Mateo: {ganancia_m}\n")

    def test_50():
        monedas = cargar_monedas(os.path.join(RUTA_DATOS, "50.txt"))
        jugadas, ganancia_s, ganancia_m = jugar(monedas)
        assert ganancia_s > ganancia_m, f"Falló en 50: S={ganancia_s} <= M={ganancia_m}"
        print("Test 50 Monedas: OK")
        print(f"Ganancia de Sophia: {ganancia_s}")
        print(f"Ganancia de Mateo: {ganancia_m}\n")

    def test_100():
        monedas = cargar_monedas(os.path.join(RUTA_DATOS, "100.txt"))
        jugadas, ganancia_s, ganancia_m = jugar(monedas)
        assert (
            ganancia_s > ganancia_m
        ), f"Falló en 100: S={ganancia_s} <= M={ganancia_m}"
        print("Test 100 Monedas: OK")
        print(f"Ganancia de Sophia: {ganancia_s}")
        print(f"Ganancia de Mateo: {ganancia_m}\n")

    def test_1000():
        monedas = cargar_monedas(os.path.join(RUTA_DATOS, "1000.txt"))
        jugadas, ganancia_s, ganancia_m = jugar(monedas)
        assert (
            ganancia_s > ganancia_m
        ), f"Falló en 1000: S={ganancia_s} <= M={ganancia_m}"
        print("Test 1000 Monedas: OK")
        print(f"Ganancia de Sophia: {ganancia_s}")
        print(f"Ganancia de Mateo: {ganancia_m}\n")

    def test_10000():
        monedas = cargar_monedas(os.path.join(RUTA_DATOS, "10000.txt"))
        jugadas, ganancia_s, ganancia_m = jugar(monedas)
        assert (
            ganancia_s > ganancia_m
        ), f"Falló en 10000: S={ganancia_s} <= M={ganancia_m}"
        print("Test 10000 Monedas: OK")
        print(f"Ganancia de Sophia: {ganancia_s}")
        print(f"Ganancia de Mateo: {ganancia_m}\n")

    def test_20000():
        monedas = cargar_monedas(os.path.join(RUTA_DATOS, "20000.txt"))
        jugadas, ganancia_s, ganancia_m = jugar(monedas)
        assert (
            ganancia_s > ganancia_m
        ), f"Falló en 20000: S={ganancia_s} <= M={ganancia_m}"
        print("Test 20000 Monedas: OK")
        print(f"Ganancia de Sophia: {ganancia_s}")
        print(f"Ganancia de Mateo: {ganancia_m}\n")

    test_20()
    test_25()
    test_50()
    test_100()
    test_1000()
    test_10000()
    test_20000()


def tests_propios():
    def test_1():
        monedas = cargar_monedas(os.path.join(RUTA_DATOS, "1.txt"))
        jugadas, ganancia_s, ganancia_m = jugar(monedas)
        assert (
            ganancia_s > ganancia_m
        ), f"Falló en 1 Moneda: S={ganancia_s} <= M={ganancia_m}"
        print("Test 1 Moneda: OK")
        print(f"Ganancia de Sophia: {ganancia_s}")
        print(f"Ganancia de Mateo: {ganancia_m}\n")

    def test_2():
        monedas = cargar_monedas(os.path.join(RUTA_DATOS, "2.txt"))
        jugadas, ganancia_s, ganancia_m = jugar(monedas)
        assert (
            ganancia_s > ganancia_m
        ), f"Falló en 2 Monedas: S={ganancia_s} <= M={ganancia_m}"
        print("Test 2 Monedas: OK")
        print(f"Ganancia de Sophia: {ganancia_s}")
        print(f"Ganancia de Mateo: {ganancia_m}\n")

    def test_iguales():
        monedas = cargar_monedas(os.path.join(RUTA_DATOS, "iguales.txt"))
        jugadas, ganancia_s, ganancia_m = jugar(monedas)
        assert (
            ganancia_s == ganancia_m
        ), f"Falló en Iguales: S={ganancia_s} != M={ganancia_m}"
        print("Test Monedas Iguales: OK")
        print(f"Ganancia de Sophia: {ganancia_s}")
        print(f"Ganancia de Mateo: {ganancia_m}\n")

    def test_iguales_impar():
        monedas = cargar_monedas(os.path.join(RUTA_DATOS, "iguales_impar.txt"))
        jugadas, ganancia_s, ganancia_m = jugar(monedas)
        assert (
            ganancia_s > ganancia_m
        ), f"Falló en Iguales Impar: S={ganancia_s} <= M={ganancia_m}"
        print("Test Monedas iguales y cantidad impar: OK")
        print(f"Ganancia de Sophia: {ganancia_s}")
        print(f"Ganancia de Mateo: {ganancia_m}\n")

    def test_creciente():
        monedas = cargar_monedas(os.path.join(RUTA_DATOS, "creciente.txt"))
        jugadas, ganancia_s, ganancia_m = jugar(monedas)
        assert (
            ganancia_s > ganancia_m
        ), f"Falló en Creciente: S={ganancia_s} <= M={ganancia_m}"
        print("Test Monedas Crecientes: OK")
        print(f"Ganancia de Sophia: {ganancia_s}")
        print(f"Ganancia de Mateo: {ganancia_m}\n")

    test_1()
    test_2()
    test_iguales()
    test_iguales_impar()
    test_creciente()


if __name__ == "__main__":
    print("\nTests Catedra.")
    tests_catedra()
    print("\nTests Propios.")
    tests_propios()
    print("\nTodos los tests pasaron exitosamente.")
