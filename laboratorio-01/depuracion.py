producto =str(input("Ingrese el nombre del producto: "))
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad de productos: "))

subtotal = cantidad * precio
print("producto:", producto)
print("subtotal: $", subtotal)