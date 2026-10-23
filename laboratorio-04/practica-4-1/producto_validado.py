class Producto:
    def __init__(self, nombre, precio):
        if nombre.strip() == "":
            raise ValueError("El nombre es obligatorio.")
        if precio <= 0:
            raise ValueError("El precio debe ser positivo.")

        self.nombre = nombre
        self.precio = precio


if __name__ == "__main__":
    try:
        producto = Producto("Teclado", -5000)
        print(producto.nombre)
    except ValueError as error:
        print("No se pudo crear:", error)
