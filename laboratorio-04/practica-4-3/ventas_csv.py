import csv
from pathlib import Path

ventas = [
    {"codigo": "V001", "producto": "Teclado", "cantidad": 2, "total": 170000.0},
    {"codigo": "V002", "producto": "Mouse", "cantidad": 1, "total": 45000.0},
    {"codigo": "V003", "producto": "Monitor", "cantidad": 1, "total": 700000.0},
    {"codigo": "V004", "producto": "Cable HDMI", "cantidad": 3, "total": 45000.0}
]

ruta = Path("ventas.csv")

with ruta.open("w", newline="", encoding="utf-8") as f:
    campos = ["codigo", "producto", "cantidad", "total"]
    escritor = csv.DictWriter(f, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(ventas)

total_recaudado = 0.0
with ruta.open("r", newline="", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        total_recaudado += float(fila["total"])

print(f"Total vendido consolidado desde CSV: ${total_recaudado:.2f}")
