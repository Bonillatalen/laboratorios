import json
from pathlib import Path

ruta = Path("productos_invalido.json")
ruta.write_text('[\n  {"codigo": "P001", "nombre": "Teclado"}\n  {"codigo": "P002"}\n]', encoding="utf-8")

try:
    with ruta.open("r", encoding="utf-8") as archivo:
        productos = json.load(archivo)
except json.JSONDecodeError as error:
    print("El archivo no contiene JSON válido. Detalle del error:", error)
