productos = []

productos.append("Teclado")
productos.append("Mouse")
productos.append("Monitor")

print(productos)
print("Cantidad:", len(productos))

nuevo_producto = input("Producto nuevo: ").strip()
productos.append(nuevo_producto)

print(productos)