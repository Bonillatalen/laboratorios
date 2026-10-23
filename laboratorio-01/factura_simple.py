producto = "Teclado"
precio_unitario = 85000.0
cantidad = 3
descuento = 0.10

subtotal = precio_unitario * cantidad
valor_descuento = subtotal * descuento
total = subtotal - valor_descuento

print("Producto:", producto)
print("Precio unitario:", precio_unitario)
print("Cantidad:", cantidad)
print("Subtotal:", subtotal)
print("Descuento:", valor_descuento)
print("Total:", total)