import json
from pathlib import Path

ruta = Path("productos.json")

if not ruta.exists():
    print("Escenario 1: El archivo no existe. Iniciando lista vacía.")
    productos = []
else:
    try:
        with ruta.open("r", encoding="utf-8") as f:
            productos = json.load(f)
        print("Escenario 2: Archivo válido cargado. Registros:", len(productos))
    except json.JSONDecodeError:
        print("Escenario 3: Archivo dañado. Se cancela carga y NO se sobrescribe el archivo.")
        print("Revisa manualmente el contenido de:", ruta.resolve())
