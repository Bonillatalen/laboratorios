
productos = [
    {"nombre": "Teclado", "categoria": "Periféricos"},
    {"nombre": "Mouse", "categoria": "Periféricos"},
    {"nombre": "Disco", "categoria": "Componentes"}
]

categorias = {producto["categoria"] for producto in productos}

print("Categorías diferentes:", categorias)
