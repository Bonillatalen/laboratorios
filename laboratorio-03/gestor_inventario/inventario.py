"""Colección y operaciones del inventario orientado a objetos."""


class Inventario:
    def __init__(self):
        # Es un atributo de instancia: cada Inventario tiene su propia lista.
        self._productos = []

    def buscar_por_codigo(self, codigo):
        return next((producto for producto in self._productos
                     if producto.codigo == codigo), None)

    def registrar_producto(self, producto):
        if self.buscar_por_codigo(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        return True

    def listar_productos(self):
        return self._productos.copy()

    def actualizar_existencias(self, codigo, nueva_cantidad):
        producto = self.buscar_por_codigo(codigo)
        if producto is None:
            return False
        producto.actualizar_existencias(nueva_cantidad)
        return True

    def eliminar_producto(self, codigo):
        producto = self.buscar_por_codigo(codigo)
        if producto is None:
            return False
        self._productos.remove(producto)
        return True

    def productos_sin_stock(self):
        return [producto.nombre for producto in self._productos
                if producto.cantidad == 0]

    def resumen(self):
        return {
            "total_productos": len(self._productos),
            "unidades_disponibles": sum(p.cantidad for p in self._productos),
            "valor_total": sum(p.calcular_valor() for p in self._productos),
            "categorias_utilizadas": {p.categoria for p in self._productos},
        }
