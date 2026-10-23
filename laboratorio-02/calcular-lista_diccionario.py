productos = [
    {"nombre": "Teclado", "precio": 85000, "cantidad": 5},
    {"nombre": "Mouse", "precio": 40000, "cantidad": 3}
]

valor_inventario = 0

for producto in productos:
    valor_inventario += producto["precio"] * producto["cantidad"]

print("Valor del inventario:", valor_inventario)