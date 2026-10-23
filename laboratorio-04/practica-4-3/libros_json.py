import json
from pathlib import Path

libros = [
    {"codigo": "L001", "titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez", "anio": 1967},
    {"codigo": "L002", "titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "anio": 1605},
    {"codigo": "L003", "titulo": "El Aleph", "autor": "Jorge Luis Borges", "anio": 1949}
]

ruta = Path("libros.json")

with ruta.open("w", encoding="utf-8") as f:
    json.dump(libros, f, ensure_ascii=False, indent=4)

with ruta.open("r", encoding="utf-8") as f:
    recuperados = json.load(f)

print("Libros cargados:")
for libro in recuperados:
    print(f"[{libro['codigo']}] {libro['titulo']} ({libro['anio']}) - {libro['autor']}")
