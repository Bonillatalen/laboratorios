import csv
from pathlib import Path

productos = [
    {"codigo": "P001", "nombre": "Teclado", "precio": 85000, "cantidad": 4},
    {"codigo": "P002", "nombre": "Mouse", "precio": 45000, "cantidad": 0}
]

ruta = Path("reporte.csv")

with ruta.open("w", newline="", encoding="utf-8") as archivo:
    campos = ["codigo", "nombre", "precio", "cantidad"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(productos)

print("Reporte exportado:", ruta)
