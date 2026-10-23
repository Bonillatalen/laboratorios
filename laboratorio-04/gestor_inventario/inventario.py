"""Operaciones de negocio del inventario, sin acceso a archivos ni input."""

from producto import Producto


class Inventario:
    def __init__(self, productos=None):
        self._productos = []
        if productos is not None:
            self.cargar_desde_lista_diccionarios(productos)

    def buscar_por_codigo(self, codigo):
        return next((p for p in self._productos if p.codigo == codigo), None)

    def registrar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("Se esperaba un objeto Producto.")
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
        return [p.nombre for p in self._productos if p.cantidad == 0]

    def resumen(self):
        return {
            "total_productos": len(self._productos),
            "unidades_disponibles": sum(p.cantidad for p in self._productos),
            "valor_total": sum(p.calcular_valor() for p in self._productos),
            "categorias_utilizadas": {p.categoria for p in self._productos},
        }

    def exportar_datos(self):
        return [p.a_diccionario() for p in self._productos]

    def cargar_desde_lista_diccionarios(self, datos):
        if not isinstance(datos, list):
            raise ValueError("El JSON debe contener una lista de productos.")
        productos_nuevos = []
        codigos = set()
        for registro in datos:
            producto = Producto.desde_diccionario(registro)
            if producto.codigo in codigos:
                raise ValueError(f"Código duplicado en el archivo: {producto.codigo}")
            codigos.add(producto.codigo)
            productos_nuevos.append(producto)
        self._productos = productos_nuevos
