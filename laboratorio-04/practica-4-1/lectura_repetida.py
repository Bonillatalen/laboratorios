while True:
    try:
        precio = float(input("Precio: "))
    except ValueError:
        print("Debes escribir un número.")
        continue

    if precio <= 0:
        print("El precio debe ser positivo.")
        continue

    print("Precio aceptado:", precio)
    break
