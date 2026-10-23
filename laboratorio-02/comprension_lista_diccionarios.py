productos = [
    {"nombre": "Teclado", "precio": 85000, "cantidad": 4},
    {"nombre": "Mouse", "precio": 45000, "cantidad": 0},
    {"nombre": "Monitor", "precio": 700000, "cantidad": 2}
]

disponibles = [
    producto["nombre"]
    for producto in productos
    if producto["cantidad"] > 0
]

print(disponibles)

valores = [
    producto["precio"] * producto["cantidad"]
    for producto in productos
]

print("Valor total:", sum(valores))