import csv
import json
from pathlib import Path

RUTA_JSON = Path("inventario.json")
RUTA_CSV = Path("inventario.csv")


def guardar_json(productos):
    with RUTA_JSON.open("w", encoding="utf-8") as f:
        json.dump(productos, f, ensure_ascii=False, indent=4)
    print("Guardado en JSON exitoso.")


def cargar_json():
    if not RUTA_JSON.exists():
        return []
    try:
        with RUTA_JSON.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("ADVERTENCIA: Archivo JSON dañado. No se cargaron datos para evitar sobrescritura.")
        return None


def exportar_csv(productos):
    if not productos:
        print("No hay productos para exportar.")
        return
    with RUTA_CSV.open("w", newline="", encoding="utf-8") as f:
        campos = ["codigo", "nombre", "precio", "cantidad"]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(productos)
    print("Exportación a CSV completada.")


if __name__ == "__main__":
    lista = [
        {"codigo": "P001", "nombre": "Teclado", "precio": 85000, "cantidad": 4},
        {"codigo": "P002", "nombre": "Mouse", "precio": 45000, "cantidad": 5}
    ]
    guardar_json(lista)
    recuperados = cargar_json()
    if recuperados is not None:
        print(f"Recuperados {len(recuperados)} productos.")
        exportar_csv(recuperados)
