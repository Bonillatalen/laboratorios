import json

# JSON corregido: agregando la coma separadora entre los elementos del arreglo
json_valido = """[
  {"codigo": "P001", "nombre": "Teclado"},
  {"codigo": "P002", "nombre": "Mouse"}
]"""

datos = json.loads(json_valido)
print("JSON corregido exitosamente. Elementos parseados:", len(datos))
