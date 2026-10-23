categorias = ("Periféricos", "Componentes", "Accesorios", "Almacenamiento")

print("--- CATEGORÍAS DISPONIBLES ---")

for i in range(len(categorias)):
    print(f"{i + 1}. {categorias[i]}")

elegida = input("\nEscribe una categoría: ").strip()

if elegida in categorias:
    print("La categoría es válida.")
else:
    print("La categoría no está registrada.")


print("Cantidad de categorías disponibles:", len(categorias))
