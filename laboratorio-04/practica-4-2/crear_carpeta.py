from pathlib import Path

carpeta = Path("datos")
carpeta.mkdir(parents=True, exist_ok=True)

ruta = carpeta / "inventario.txt"
ruta.write_text("Inventario inicial\n", encoding="utf-8")
print("Ubicación:", ruta)
