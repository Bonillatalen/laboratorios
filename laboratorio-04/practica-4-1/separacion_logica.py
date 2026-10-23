try:
    cantidad = int(input("Cantidad: "))
except ValueError:
    print("No es un número entero.")
else:
    if cantidad < 0:
        print("No se aceptan existencias negativas.")
    else:
        print("Cantidad aceptada:", cantidad)
