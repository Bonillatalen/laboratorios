"""Interacción por consola del gestor persistente."""

from almacenamiento import ErrorAlmacenamiento, cargar_inventario, guardar_inventario
from inventario import Inventario
from producto import CATEGORIAS, Producto
from reportes import exportar_csv


def mostrar_menu():
    print("\n=== GESTOR DE INVENTARIO PERSISTENTE ===")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Resumen")
    print("7. Exportar reporte CSV")
    print("0. Guardar y salir")


def leer_precio():
    while True:
        try:
            valor = float(input("Precio: ").strip())
            if valor <= 0:
                raise ValueError
            return valor
        except ValueError:
            print("Ingresa un precio numérico mayor que cero.")


def leer_cantidad(mensaje="Cantidad: "):
    while True:
        try:
            valor = int(input(mensaje).strip())
            if valor < 0:
                raise ValueError
            return valor
        except ValueError:
            print("Ingresa una cantidad entera no negativa.")


def guardar_con_mensaje(inventario):
    try:
        ruta = guardar_inventario(inventario)
        print(f"Inventario guardado en {ruta.name}.")
    except ErrorAlmacenamiento as error:
        print(f"Error de almacenamiento: {error}")


def main():
    try:
        inventario = cargar_inventario()
    except ErrorAlmacenamiento as error:
        print(f"No se puede iniciar sin revisar los datos: {error}")
        return

    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()
        try:
            if opcion == "1":
                print("Categorías:", ", ".join(CATEGORIAS))
                producto = Producto(
                    input("Código: ").strip(), input("Nombre: ").strip(),
                    input("Categoría: ").strip(), leer_precio(), leer_cantidad()
                )
                if inventario.registrar_producto(producto):
                    guardar_con_mensaje(inventario)
                    print("Producto registrado.")
                else:
                    print("Ya existe un producto con ese código.")
            elif opcion == "2":
                productos = inventario.listar_productos()
                print("\n".join(map(str, productos)) if productos else "Inventario vacío.")
            elif opcion == "3":
                producto = inventario.buscar_por_codigo(input("Código: ").strip())
                print(producto if producto else "Producto no encontrado.")
            elif opcion == "4":
                codigo = input("Código: ").strip()
                if inventario.actualizar_existencias(codigo, leer_cantidad("Nueva cantidad: ")):
                    guardar_con_mensaje(inventario)
                    print("Existencias actualizadas.")
                else:
                    print("Producto no encontrado.")
            elif opcion == "5":
                if inventario.eliminar_producto(input("Código: ").strip()):
                    guardar_con_mensaje(inventario)
                    print("Producto eliminado.")
                else:
                    print("Producto no encontrado.")
            elif opcion == "6":
                resumen = inventario.resumen()
                print(f"Productos: {resumen['total_productos']}")
                print(f"Unidades: {resumen['unidades_disponibles']}")
                print(f"Valor total: ${resumen['valor_total']:.2f}")
            elif opcion == "7":
                print(f"Reporte creado en {exportar_csv(inventario).name}.")
            elif opcion == "0":
                guardar_con_mensaje(inventario)
                print("Programa finalizado.")
                break
            else:
                print("Opción no válida.")
        except (ValueError, OSError, ErrorAlmacenamiento) as error:
            print(f"No se pudo completar la operación: {error}")


if __name__ == "__main__":
    main()
