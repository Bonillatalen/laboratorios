from pathlib import Path

# Corrección: Usar append ("a") para no destruir registros anteriores
ruta = Path("historial.txt")

with open(ruta, "a", encoding="utf-8") as f:
    f.write("Registro 1\n")
    f.write("Registro 2\n")

print(ruta.read_text(encoding="utf-8"))
