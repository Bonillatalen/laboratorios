
productos = ["Teclado", "Mouse", "Monitor"]
nuevos = ["Impresora", "Cámara"]

productos[1] = "Mouse inalámbrico"
print("Paso 1:", productos)

productos.insert(0, "Parlantes")
print("Paso 2:", productos)

productos.extend(nuevos)
print("Paso 3:", productos)

productos.remove("Monitor")
print("Paso 4:", productos)

eliminado = productos.pop()
print("Elemento extraído:", eliminado)
print("Paso 5:", productos)
