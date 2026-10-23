import csv
from pathlib import Path

ruta = Path("reporte.csv")

if ruta.exists():
    with ruta.open("r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for producto in lector:
            print(f"Código: {producto['codigo']} | Nombre: {producto['nombre']} | Precio: ${float(producto['precio']):.2f}")
else:
    print("reporte.csv no existe.")
