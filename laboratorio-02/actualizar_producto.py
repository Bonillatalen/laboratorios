
producto = {
    "codigo": "P001",
    "nombre": "Teclado",
    "precio": 85000,
    "cantidad": 5
}

nuevo_precio = float(input("Ingresa el nuevo precio: "))

if nuevo_precio > 0:
    producto["precio"] = nuevo_precio
    print("Precio actualizado correctamente.")
else:
    print("El precio debe ser mayor que cero.")

print("\nInformación del producto:")

for clave, valor in producto.items():
    print(clave, ":", valor)
