from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_HISTORIAL = BASE_DIR / "operaciones.txt"


def registrar_operacion():
    concepto = input("Concepto: ").strip()
    try:
        valor = float(input("Valor: "))
    except ValueError:
        print("Valor inválido. Operación cancelada.")
        return

    with open(RUTA_HISTORIAL, "a", encoding="utf-8") as f:
        f.write(f"{concepto};{valor}\n")
    print("Operación registrada con éxito.")


def mostrar_historial():
    if not RUTA_HISTORIAL.exists():
        print("Aún no existe historial de operaciones.")
        return

    with open(RUTA_HISTORIAL, "r", encoding="utf-8") as f:
        lineas = f.readlines()

    if not lineas:
        print("El historial está vacío.")
        return

    print("\n--- Historial de Operaciones ---")
    for i, linea in enumerate(lineas, start=1):
        datos = linea.strip().split(";")
        if len(datos) == 2:
            print(f"{i}. Concepto: {datos[0]} | Valor: ${float(datos[1]):.2f}")


def main():
    while True:
        print("\n1. Registrar operación\n2. Mostrar historial\n0. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            registrar_operacion()
        elif opcion == "2":
            mostrar_historial()
        elif opcion == "0":
            print("Fin del programa.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
