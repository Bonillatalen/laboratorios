import json

producto = {"nombre": "Cámara", "precio": 120000}

texto = json.dumps(producto, ensure_ascii=False)
recuperado = json.loads(texto)

print("Texto serializado:", texto)
print("Propiedad deserializada:", recuperado["nombre"])
