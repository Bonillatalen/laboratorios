from pathlib import Path

ruta = Path("pruebas.txt")

if ruta.exists():
    with open(ruta, "r", encoding="utf-8") as archivo:
        for numero, linea in enumerate(archivo, start=1):
            print(numero, "-", linea.strip())
else:
    print("pruebas.txt no existe. Ejecuta bitacora.py primero.")
