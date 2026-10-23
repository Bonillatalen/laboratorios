ventas = [
    {"producto": "Teclado", "categoria": "Periféricos", "total": 150000},
    {"producto": "Mouse", "categoria": "Periféricos", "total": 70000},
    {"producto": "Disco SSD", "categoria": "Componentes", "total": 280000},
    {"producto": "Memoria USB", "categoria": "Accesorios", "total": 45000}
]

ventas_altas = [
    venta["producto"] for venta in ventas
    if venta["total"] > 100000
]

categorias = {venta["categoria"] for venta in ventas}

resumen_ventas = {
    venta["producto"]: venta["total"]
    for venta in ventas
}

print("Ventas superiores a $100.000:", ventas_altas)
print("Categorías diferentes:", categorias)
print("Resumen de ventas:", resumen_ventas)
