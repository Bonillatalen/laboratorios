try:
    cantidad = int(input("Cantidad de productos: "))
    print("Cantidad registrada:", cantidad)
except ValueError:
    print("Debes escribir un número entero.")

print("Fin del programa.")
