import unittest

from inventario import Inventario
from producto import Producto


class GestorOrientadoObjetosTest(unittest.TestCase):
    def crear_producto(self, codigo="P001", cantidad=4):
        return Producto(codigo, "Teclado", "Periféricos", 85000, cantidad)

    def test_producto_tiene_propiedades_y_calcula_valor(self):
        producto = self.crear_producto()
        self.assertEqual(producto.codigo, "P001")
        self.assertEqual(producto.calcular_valor(), 340000)

    def test_propiedades_rechazan_datos_incorrectos(self):
        with self.assertRaises(ValueError):
            Producto("P002", "Mouse", "Jardín", 100, 1)
        with self.assertRaises(ValueError):
            Producto("P003", "Mouse", "Periféricos", 0, 1)
        with self.assertRaises(ValueError):
            Producto("P004", "Mouse", "Periféricos", 100, -1)
        producto = self.crear_producto()
        with self.assertRaises(ValueError):
            producto.precio = -10
        self.assertEqual(producto.precio, 85000)

    def test_registro_busqueda_actualizacion_y_eliminacion(self):
        inventario = Inventario()
        producto = self.crear_producto()
        self.assertTrue(inventario.registrar_producto(producto))
        self.assertFalse(inventario.registrar_producto(self.crear_producto("P001")))
        self.assertIs(inventario.buscar_por_codigo("P001"), producto)
        self.assertTrue(inventario.actualizar_existencias("P001", 9))
        self.assertEqual(producto.cantidad, 9)
        self.assertTrue(inventario.eliminar_producto("P001"))
        self.assertIsNone(inventario.buscar_por_codigo("P001"))

    def test_inventarios_mantienen_colecciones_independientes(self):
        primero = Inventario()
        segundo = Inventario()
        primero.registrar_producto(self.crear_producto())
        self.assertEqual(len(primero.listar_productos()), 1)
        self.assertEqual(len(segundo.listar_productos()), 0)
        self.assertIsNot(primero.listar_productos(), segundo.listar_productos())

    def test_resumen_productos_agotados_y_return(self):
        inventario = Inventario()
        inventario.registrar_producto(self.crear_producto("P001", 4))
        inventario.registrar_producto(Producto("P002", "Mouse", "Accesorios", 40000, 0))
        resumen = inventario.resumen()
        self.assertEqual(resumen["total_productos"], 2)
        self.assertEqual(resumen["unidades_disponibles"], 4)
        self.assertEqual(resumen["valor_total"], 340000.0)
        self.assertEqual(inventario.productos_sin_stock(), ["Mouse"])


if __name__ == "__main__":
    unittest.main()
