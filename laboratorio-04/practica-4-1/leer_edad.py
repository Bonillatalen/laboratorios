try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Error: La edad debe ser un número entero.")
else:
    if edad < 0:
        print("Error: La edad no puede ser negativa.")
    elif edad > 120:
        print("Error: La edad no puede ser superior a 120 años.")
    else:
        print(f"Edad validada y registrada: {edad}")
