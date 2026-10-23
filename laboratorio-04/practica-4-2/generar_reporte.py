from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
carpeta_reportes = BASE_DIR / "reportes"
carpeta_reportes.mkdir(parents=True, exist_ok=True)

ruta_archivo = carpeta_reportes / "resumen.txt"
contenido = (
    "Reporte de Estado del Sistema\n"
    "Total módulos verificados: 5\n"
    "Operaciones exitosas: 100%\n"
)

ruta_archivo.write_text(contenido, encoding="utf-8")

contenido_leido = ruta_archivo.read_text(encoding="utf-8")
print("Contenido leído:")
print(contenido_leido)
print("Ruta de guardado:", ruta_archivo)
