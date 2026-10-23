"""Gestor de inventario del Laboratorio 02."""

CATEGORIAS_PERMITIDAS = {"Periféricos", "Componentes", "Accesorios", "Oficina"}


def buscar_producto(productos, codigo):
    """Devuelve el producto cuyo código coincide o None si no existe."""
    return next((producto for producto in productos if producto["codigo"] == codigo), None)


def validar_producto(productos, codigo, nombre, categoria, precio, cantidad,
                     codigo_original=None):
    """Valida los datos de un producto antes de registrarlo o actualizarlo."""
    if not codigo.strip() or not nombre.strip():
        raise ValueError("El código y el nombre son obligatorios")
    repetido = buscar_producto(productos, codigo)
    if repetido is not None and codigo != codigo_original:
        raise ValueError("Ya existe un producto con ese código")
    if categoria not in CATEGORIAS_PERMITIDAS:
        raise ValueError("La categoría no está permitida")
    if precio <= 0:
        raise ValueError("El precio debe ser mayor que cero")
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa")


def registrar_producto(productos, codigo, nombre, categoria, precio, cantidad):
    validar_producto(productos, codigo, nombre, categoria, precio, cantidad)
    producto = {
        "codigo": codigo.strip(),
        "nombre": nombre.strip(),
        "categoria": categoria,
        "precio": float(precio),
        "cantidad": int(cantidad),
    }
    productos.append(producto)
    return producto


def consultar_productos(productos):
    """Devuelve una copia de la colección para consultar sin modificarla."""
    return list(productos)


def actualizar_producto(productos, codigo, nombre=None, categoria=None,
                        precio=None, cantidad=None):
    producto = buscar_producto(productos, codigo)
    if producto is None:
        raise KeyError("No se encontró el producto")
    nuevo_nombre = producto["nombre"] if nombre is None else nombre
    nueva_categoria = producto["categoria"] if categoria is None else categoria
    nuevo_precio = producto["precio"] if precio is None else precio
    nueva_cantidad = producto["cantidad"] if cantidad is None else cantidad
    validar_producto(productos, codigo, nuevo_nombre, nueva_categoria,
                     nuevo_precio, nueva_cantidad, codigo_original=codigo)
    producto.update({
        "nombre": nuevo_nombre.strip(),
        "categoria": nueva_categoria,
        "precio": float(nuevo_precio),
        "cantidad": int(nueva_cantidad),
    })
    return producto


def eliminar_producto(productos, codigo):
    producto = buscar_producto(productos, codigo)
    if producto is None:
        raise KeyError("No se encontró el producto")
    productos.remove(producto)
    return producto


def obtener_categorias(productos):
    return {producto["categoria"] for producto in productos}


def generar_informe(productos):
    """Genera consultas agrupadas y el valor económico del inventario."""
    por_categoria = {
        categoria: sum(p["cantidad"] for p in productos
                       if p["categoria"] == categoria)
        for categoria in obtener_categorias(productos)
    }
    valor_total = sum(p["precio"] * p["cantidad"] for p in productos)
    productos_agotados = [p["nombre"] for p in productos if p["cantidad"] == 0]
    return {
        "total_productos": len(productos),
        "unidades_totales": sum(p["cantidad"] for p in productos),
        "categorias": obtener_categorias(productos),
        "unidades_por_categoria": por_categoria,
        "valor_total": valor_total,
        "productos_agotados": productos_agotados,
    }


def mostrar_productos(productos):
    if not productos:
        print("No hay productos registrados.")
        return
    for producto in productos:
        print(
            f"{producto['codigo']} | {producto['nombre']} | "
            f"{producto['categoria']} | ${producto['precio']:.2f} | "
            f"Cantidad: {producto['cantidad']}"
        )


def pedir_numero(mensaje, conversion):
    try:
        return conversion(input(mensaje))
    except ValueError as error:
        raise ValueError("Debe ingresar un valor numérico válido") from error


def menu():
    productos = []
    while True:
        print("\n--- GESTOR DE INVENTARIO ---")
        print("1. Registrar producto")
        print("2. Consultar productos")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Ver informe")
        print("0. Salir")
        opcion = input("Seleccione una opción: ").strip()
        try:
            if opcion == "1":
                registrar_producto(
                    productos,
                    input("Código: ").strip(),
                    input("Nombre: ").strip(),
                    input(f"Categoría ({', '.join(sorted(CATEGORIAS_PERMITIDAS))}): "),
                    pedir_numero("Precio: ", float),
                    pedir_numero("Cantidad: ", int),
                )
                print("Producto registrado correctamente.")
            elif opcion == "2":
                mostrar_productos(consultar_productos(productos))
            elif opcion == "3":
                encontrado = buscar_producto(productos, input("Código: ").strip())
                print(encontrado if encontrado else "No se encontró el producto.")
            elif opcion == "4":
                codigo = input("Código del producto: ").strip()
                actualizar_producto(
                    productos, codigo,
                    nombre=input("Nuevo nombre: ").strip(),
                    categoria=input("Nueva categoría: ").strip(),
                    precio=pedir_numero("Nuevo precio: ", float),
                    cantidad=pedir_numero("Nueva cantidad: ", int),
                )
                print("Producto actualizado correctamente.")
            elif opcion == "5":
                eliminar_producto(productos, input("Código: ").strip())
                print("Producto eliminado correctamente.")
            elif opcion == "6":
                informe = generar_informe(productos)
                print(f"Productos registrados: {informe['total_productos']}")
                print(f"Unidades totales: {informe['unidades_totales']}")
                print(f"Categorías: {', '.join(sorted(informe['categorias'])) or 'Ninguna'}")
                print(f"Valor del inventario: ${informe['valor_total']:.2f}")
                print(f"Agotados: {informe['productos_agotados'] or 'Ninguno'}")
            elif opcion == "0":
                print("Programa finalizado.")
                break
            else:
                print("Opción no válida.")
        except (ValueError, KeyError) as error:
            print(f"No se pudo completar la operación: {error}")


if __name__ == "__main__":
    menu()
