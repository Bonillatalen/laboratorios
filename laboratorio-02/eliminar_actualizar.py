producto = {
    "codigo": "P001",
    "nombre": "Teclado",
    "precio": 85000.0,
    "cantidad": 4
}

producto.update({"precio": 80000.0, "cantidad": 5})
cantidad_eliminada = producto.pop("cantidad")

print(producto)
print("Cantidad eliminada:", cantidad_eliminada)