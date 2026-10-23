from pathlib import Path

ruta = Path("mensaje.txt")
ruta.write_text("Primer archivo de Python.\n", encoding="utf-8")
print("Archivo guardado:", ruta)
