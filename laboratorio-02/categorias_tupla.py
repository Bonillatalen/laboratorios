categorias = ("Periféricos", "Componentes", "Accesorios")

for categoria in categorias:
    print(categoria)

elegida = input("Categoría: ").strip()

if elegida in categorias:
    print("Categoría válida.")
else:
    print("Categoría no registrada.")
    