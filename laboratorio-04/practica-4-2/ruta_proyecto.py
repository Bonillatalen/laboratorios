from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_DATOS = BASE_DIR / "datos" / "inventario.txt"

RUTA_DATOS.parent.mkdir(parents=True, exist_ok=True)
RUTA_DATOS.write_text("Datos del proyecto\n", encoding="utf-8")
print("Archivo generado en:", RUTA_DATOS)
