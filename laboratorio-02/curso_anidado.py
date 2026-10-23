
curso = {
    "nombre": "Análisis y Desarrollo de Software",
    "codigo": "ADSO101",
    "temas": ["Python", "Bases de datos", "Programación web"],
    "instructor": {
        "nombre": "Carlos Pérez",
        "correo": "carlos@gmail.com"
    }
}

print("Nombre del curso:", curso["nombre"])
print("Segundo tema:", curso["temas"][1])
print("Nombre del instructor:", curso["instructor"]["nombre"])
print("Cantidad de temas:", len(curso["temas"]))
