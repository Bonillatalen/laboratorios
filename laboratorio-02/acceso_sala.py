
edad = int(input("Ingresa tu edad: "))
autorizacion = input("¿Tienes autorización? (si/no): ").strip().lower()

if edad >= 18:
    print("Acceso permitido.")
elif autorizacion == "si":
    print("Acceso permitido.")
else:
    print("Acceso no permitido.")
