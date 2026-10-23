
edad = int(input("Ingresa tu edad: "))
inscripcion = input("¿Estás inscrito? (si/no): ").strip().lower()
documentos = int(input("¿Cuántos documentos entregaste?: "))

if edad < 16:
    print("Te falta cumplir con la edad mínima de 16 años.")

if inscripcion != "si":
    print("Debes estar inscrito.")

if documentos < 3:
    print("Debes entregar al menos 3 documentos.")

if edad >= 16 and inscripcion == "si" and documentos >= 3:
    print("La solicitud cumple todos los requisitos.")
else:
    print("La solicitud no cumple todos los requisitos.")
