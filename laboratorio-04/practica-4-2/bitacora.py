nombre_prueba = input("Nombre de la prueba: ").strip()
resultado = input("Resultado (aprobada/fallida): ").strip()
observacion = input("Observación breve: ").strip()

registro = f"{nombre_prueba} | {resultado} | {observacion}\n"

with open("pruebas.txt", "a", encoding="utf-8") as archivo:
    archivo.write(registro)

print("Registro guardado en pruebas.txt")
