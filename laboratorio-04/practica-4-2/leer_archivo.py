from pathlib import Path

ruta = Path("mensaje.txt")

try:
    contenido = ruta.read_text(encoding="utf-8")
    print("Contenido:\n" + contenido)
except FileNotFoundError:
    print("El archivo mensaje.txt no existe.")
