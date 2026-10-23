"""Entidad Producto del gestor orientado a objetos."""

CATEGORIAS = ("Periféricos", "Componentes", "Accesorios", "Oficina")


class Producto:
    def __init__(self, codigo, nombre, categoria, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

    @staticmethod
    def _texto_valido(valor, campo):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"El {campo} no puede estar vacío.")
        return valor.strip()

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        self._codigo = self._texto_valido(valor, "código")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = self._texto_valido(valor, "nombre")

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        if valor not in CATEGORIAS:
            raise ValueError(f"Categoría inválida. Debe ser una de: {CATEGORIAS}")
        self._categoria = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        try:
            valor = float(valor)
        except (TypeError, ValueError) as error:
            raise ValueError("El precio debe ser numérico.") from error
        if valor <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self._precio = valor

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        try:
            valor = int(valor)
        except (TypeError, ValueError) as error:
            raise ValueError("La cantidad debe ser un número entero.") from error
        if valor < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self._cantidad = valor

    def actualizar_existencias(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def calcular_valor(self):
        return self.precio * self.cantidad

    def __str__(self):
        return (f"{self.codigo} - {self.nombre} - {self.categoria} - "
                f"${self.precio:.2f} - {self.cantidad} unidades")
