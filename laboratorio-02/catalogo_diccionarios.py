productos = [
    {"nombre": "Teclado", "precio": 85000, "cantidad": 5},
    {"nombre": "Mouse", "precio": 40000, "cantidad": 3},
    {"nombre": "Monitor", "precio": 500000, "cantidad": 2}
]

nombre = input("Nombre del producto: ")
precio = float(input("Precio del producto: "))
cantidad = int(input("Cantidad disponible: "))

nuevo_producto = {
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad
}

productos.append(nuevo_producto)

print("\n--- CATÁLOGO DE PRODUCTOS ---")

for producto in productos:
    print(producto)
