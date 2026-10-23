
def mostrar_productos(productos):
    print("--- INVENTARIO DISPONIBLE ---")
    for p in productos:
        print(f"[{p['codigo']}] {p['nombre']} - Precio: ${p['precio']} - Stock: {p['cantidad']}")
    print("-----------------------------")


def buscar_producto(productos, codigo):
    for p in productos:
        if p["codigo"] == codigo:
            return p
    return None


def valor_inventario(productos):
    plata_total = 0
    for p in productos:
        plata_total += p["precio"] * p["cantidad"]
    return plata_total


def productos_sin_stock(productos):
    lista_vacios = []
    for p in productos:
        if p["cantidad"] == 0:
            lista_vacios.append(p["nombre"])
    return lista_vacios


mis_productos = [
    {"codigo": "A1", "nombre": "Mouse", "precio": 40000, "cantidad": 5},
    {"codigo": "B2", "nombre": "Teclado", "precio": 90000, "cantidad": 0},
    {"codigo": "C3", "nombre": "Pantalla", "precio": 450000, "cantidad": 2}
]

mostrar_productos(mis_productos)

encontrado = buscar_producto(mis_productos, "A1")
print(f"Buscando A1: {encontrado}")

no_encontrado = buscar_producto(mis_productos, "Z9")
print(f"Buscando Z9: {no_encontrado}")

total_plata = valor_inventario(mis_productos)
print(f"Total plata invertida: ${total_plata}")

agotados = productos_sin_stock(mis_productos)
print(f"Productos que no tienen existencias: {agotados}")