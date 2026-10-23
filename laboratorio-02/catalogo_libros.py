libros = [
    {"codigo": "L001", "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "anio": 1967},
    {"codigo": "L002", "titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "anio": 1943},
    {"codigo": "L003", "titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "anio": 1605}
]

codigo_buscado = input("Ingresa el código del libro que buscas: ").strip()
encontrado = False

for libro in libros:
    if libro["codigo"] == codigo_buscado:
        print("\nLibro encontrado:")
        print("Código:", libro["codigo"])
        print("Título:", libro["titulo"])
        print("Autor:", libro["autor"])
        print("Año:", libro["anio"])
        encontrado = True
        break

if not encontrado:
    print("El libro no fue localizado.")

respuesta = input("\n¿Deseas agregar un libro? (si/no): ").strip().lower()

if respuesta == "si":
    nuevo_codigo = input("Código del nuevo libro: ").strip()

    codigo_repetido = False

    for libro in libros:
        if libro["codigo"] == nuevo_codigo:
            codigo_repetido = True
            break

    if codigo_repetido:
        print("Ese código ya existe. No se agregó el libro.")
    else:
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        anio = int(input("Año de publicación: "))

        nuevo_libro = {
            "codigo": nuevo_codigo,
            "titulo": titulo,
            "autor": autor,
            "anio": anio
        }

        libros.append(nuevo_libro)
        print("Libro agregado correctamente.")

print("\n--- CATÁLOGO DE LIBROS ---")

for libro in libros:
    print(libro)
