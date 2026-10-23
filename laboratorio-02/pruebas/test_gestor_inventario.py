import unittest

from gestor_inventario import (
    actualizar_producto,
    buscar_producto,
    eliminar_producto,
    generar_informe,
    obtener_categorias,
    registrar_producto,
)


class GestorInventarioTest(unittest.TestCase):
    def setUp(self):
        self.productos = []
        registrar_producto(self.productos, "P001", "Teclado", "Periféricos", 85000, 5)
        registrar_producto(self.productos, "P002", "Monitor", "Componentes", 500000, 2)

    def test_registro_y_busqueda(self):
        producto = buscar_producto(self.productos, "P001")
        self.assertEqual(producto["nombre"], "Teclado")
        self.assertEqual(len(self.productos), 2)

    def test_actualizacion_conserva_el_producto(self):
        actualizar_producto(self.productos, "P001", precio=90000, cantidad=8)
        producto = buscar_producto(self.productos, "P001")
        self.assertEqual(producto["precio"], 90000)
        self.assertEqual(producto["cantidad"], 8)

    def test_eliminacion(self):
        eliminado = eliminar_producto(self.productos, "P002")
        self.assertEqual(eliminado["nombre"], "Monitor")
        self.assertIsNone(buscar_producto(self.productos, "P002"))

    def test_rechaza_duplicado_categoria_precio_y_cantidad(self):
        with self.assertRaises(ValueError):
            registrar_producto(self.productos, "P001", "Otro", "Oficina", 10, 1)
        with self.assertRaises(ValueError):
            registrar_producto(self.productos, "P003", "Silla", "Jardín", 10, 1)
        with self.assertRaises(ValueError):
            registrar_producto(self.productos, "P004", "Silla", "Oficina", 0, 1)
        with self.assertRaises(ValueError):
            registrar_producto(self.productos, "P005", "Silla", "Oficina", 10, -1)

    def test_no_permite_actualizar_con_cantidad_negativa(self):
        with self.assertRaises(ValueError):
            actualizar_producto(self.productos, "P001", cantidad=-2)
        self.assertEqual(buscar_producto(self.productos, "P001")["cantidad"], 5)

    def test_categorias_sin_repetir_e_informe(self):
        self.assertEqual(obtener_categorias(self.productos), {"Periféricos", "Componentes"})
        informe = generar_informe(self.productos)
        self.assertEqual(informe["unidades_totales"], 7)
        self.assertEqual(informe["valor_total"], 1425000)
        self.assertEqual(informe["unidades_por_categoria"]["Periféricos"], 5)


if __name__ == "__main__":
    unittest.main()
