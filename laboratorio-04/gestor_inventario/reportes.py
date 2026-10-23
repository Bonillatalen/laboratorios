"""Generación de reportes CSV del inventario."""

import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_CSV = BASE_DIR / "reportes" / "inventario.csv"
CAMPOS = ("codigo", "nombre", "categoria", "precio", "cantidad", "valor_inventario")


def exportar_csv(inventario, ruta=RUTA_CSV):
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    try:
        with ruta.open("w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
            escritor.writeheader()
            for producto in inventario.listar_productos():
                escritor.writerow({
                    "codigo": producto.codigo,
                    "nombre": producto.nombre,
                    "categoria": producto.categoria,
                    "precio": f"{producto.precio:.2f}",
                    "cantidad": producto.cantidad,
                    "valor_inventario": f"{producto.calcular_valor():.2f}",
                })
    except OSError as error:
        raise OSError(f"No se pudo generar el reporte CSV: {error}") from error
    return ruta
