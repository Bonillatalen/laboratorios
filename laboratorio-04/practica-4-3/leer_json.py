import json
from pathlib import Path

ruta = Path("productos.json")

if ruta.exists():
    with ruta.open("r", encoding="utf-8") as archivo:
        productos = json.load(archivo)

    for producto in productos:
        print(producto["codigo"], "-", producto["nombre"])
else:
    print("productos.json no encontrado.")
