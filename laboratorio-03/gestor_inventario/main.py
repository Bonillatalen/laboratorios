from producto import Producto, CATEGORIAS
from inventario import Inventario

def mostrar_menu():
    print()
    print("================================")
    print("       GESTOR DE INVENTARIO")
    print("================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Consultar productos sin stock")
    print("7. Resumen del inventario")
    print("0. Salir")

def leer_precio():
    while True:
        try:
            precio = float(input("Precio: ").strip())
            if precio <= 0:
                print("El precio debe ser mayor a cero.")
                continue
            return precio
        except ValueError:
            print("Debes ingresar un número válido para el precio.")

def leer_cantidad(mensaje="Cantidad: "):
    while True:
        try:
            cantidad = int(input(mensaje).strip())
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue
            return cantidad
        except ValueError:
            print("Debes escribir un número entero.")

def main():
    inventario = Inventario()
    opcion = ""

    while opcion != "0":
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            codigo = input("Código: ").strip()
            nombre = input("Nombre: ").strip()
            print(f"Categorías: {', '.join(CATEGORIAS)}")
            categoria = input("Categoría: ").strip()
            precio = leer_precio()
            cantidad = leer_cantidad()

            try:
                nuevo_prod = Producto(codigo, nombre, categoria, precio, cantidad)
                if inventario.registrar_producto(nuevo_prod):
                    print("Producto registrado exitosamente.")
                else:
                    print("Error: Ya existe un producto con ese código.")
            except ValueError as e:
                print(f"Error de validación: {e}")

        elif opcion == "2":
            productos = inventario.listar_productos()
            if not productos:
                print("El inventario está vacío.")
            else:
                for p in productos:
                    print(f"{p.codigo} - {p.nombre} - {p.categoria} - ${p.precio:.1f} - {p.cantidad} unidades")

        elif opcion == "3":
            codigo = input("Código a buscar: ").strip()
            prod = inventario.buscar_por_codigo(codigo)
            if prod is not None:
                print(f"Encontrado: {prod.codigo} - {prod.nombre} - {prod.categoria} - ${prod.precio:.1f} - {prod.cantidad} unidades")
            else:
                print("Producto no registrado.")

        elif opcion == "4":
            codigo = input("Código a actualizar: ").strip()
            prod = inventario.buscar_por_codigo(codigo)
            if prod is None:
                print("Producto no registrado.")
            else:
                nueva_cantidad = leer_cantidad("Nueva cantidad: ")
                if inventario.actualizar_existencias(codigo, nueva_cantidad):
                    print("Existencias actualizadas.")
                else:
                    print("No se pudo actualizar las existencias.")

        elif opcion == "5":
            codigo = input("Código a eliminar: ").strip()
            if inventario.eliminar_producto(codigo):
                print("Producto eliminado correctamente.")
            else:
                print("No se encontró el producto a eliminar.")

        elif opcion == "6":
            agotados = inventario.productos_sin_stock()
            if not agotados:
                print("No hay productos sin existencias.")
            else:
                print("Sin existencias:")
                for nombre in agotados:
                    print(f"- {nombre}")

        elif opcion == "7":
            res = inventario.resumen()
            print(f"Productos registrados: {res['total_productos']}")
            print(f"Unidades disponibles: {res['unidades_disponibles']}")
            print(f"Valor del inventario: ${res['valor_total']:.1f}")
            cats = ", ".join(res["categorias_utilizadas"]) if res["categorias_utilizadas"] else "Ninguna"
            print(f"Categorías utilizadas: {cats}")

        elif opcion == "0":
            print("Programa finalizado.")
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
