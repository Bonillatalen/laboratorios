import csv
import tempfile
import unittest
from pathlib import Path

from almacenamiento import ErrorAlmacenamiento, cargar_inventario, guardar_inventario
from inventario import Inventario
from producto import Producto
from reportes import exportar_csv


class PersistenciaTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.json_path = self.root / "productos.json"
        self.csv_path = self.root / "reportes" / "inventario.csv"
        self.inventario = Inventario()
        self.inventario.registrar_producto(
            Producto("P001", "Teclado", "Periféricos", 85000, 4)
        )
        self.inventario.registrar_producto(
            Producto("P002", "Mouse", "Accesorios", 40000, 0)
        )

    def tearDown(self):
        self.temp.cleanup()

    def test_guardar_y_recuperar_despues_de_reiniciar(self):
        guardar_inventario(self.inventario, self.json_path)
        recuperado = cargar_inventario(self.json_path)
        self.assertEqual(len(recuperado.listar_productos()), 2)
        self.assertEqual(recuperado.buscar_por_codigo("P001").cantidad, 4)
        self.assertEqual(recuperado.resumen()["valor_total"], 340000)

    def test_json_danado_no_se_reemplaza_por_lista_vacia(self):
        self.json_path.write_text('{"datos":', encoding="utf-8")
        contenido_antes = self.json_path.read_text(encoding="utf-8")
        with self.assertRaises(ErrorAlmacenamiento):
            cargar_inventario(self.json_path)
        self.assertEqual(self.json_path.read_text(encoding="utf-8"), contenido_antes)

    def test_carga_rechaza_duplicados_y_precios_negativos_sin_carga_parcial(self):
        datos = [{"codigo": "P001", "nombre": "A", "categoria": "Accesorios", "precio": 1, "cantidad": 1},
                 {"codigo": "P001", "nombre": "B", "categoria": "Accesorios", "precio": 2, "cantidad": 1}]
        self.json_path.write_text(__import__("json").dumps(datos), encoding="utf-8")
        with self.assertRaises(ErrorAlmacenamiento):
            cargar_inventario(self.json_path)
        datos[1]["codigo"] = "P002"
        datos[1]["precio"] = -2
        self.json_path.write_text(__import__("json").dumps(datos), encoding="utf-8")
        with self.assertRaises(ErrorAlmacenamiento):
            cargar_inventario(self.json_path)

    def test_exportar_csv_calcula_valor_por_cantidad(self):
        exportar_csv(self.inventario, self.csv_path)
        with self.csv_path.open(encoding="utf-8", newline="") as archivo:
            filas = list(csv.DictReader(archivo))
        self.assertEqual(filas[0]["valor_inventario"], "340000.00")
        self.assertEqual(filas[1]["valor_inventario"], "0.00")
        self.assertEqual(len(filas), 2)

    def test_validaciones_del_producto(self):
        with self.assertRaises(ValueError):
            Producto("P003", "Monitor", "Oficina", -1, 1)
        with self.assertRaises(ValueError):
            Producto("P004", "Monitor", "Oficina", 1, -1)
        self.assertTrue(self.inventario.actualizar_existencias("P001", 8))
        self.assertEqual(self.inventario.buscar_por_codigo("P001").cantidad, 8)


if __name__ == "__main__":
    unittest.main()
