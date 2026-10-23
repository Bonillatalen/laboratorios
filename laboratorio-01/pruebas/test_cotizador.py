import unittest

from cotizador_compra import calcular_cotizacion


class CotizadorTest(unittest.TestCase):
    def test_caso_referencia(self):
        resultado = calcular_cotizacion(50000, 2, 10, 19, 1000)
        esperado = {
            "subtotal": 100000,
            "valor_descuento": 10000,
            "base_descuento": 90000,
            "valor_impuesto": 17100,
            "costo_envio": 1000,
            "total": 108100,
        }
        self.assertEqual(resultado, esperado)

    def test_sin_descuento_ni_impuesto(self):
        resultado = calcular_cotizacion(85000, 3, 0, 0, 1000)
        self.assertEqual(resultado["subtotal"], 255000)
        self.assertEqual(resultado["total"], 256000)

    def test_rechaza_cantidad_no_positiva(self):
        with self.assertRaises(ValueError):
            calcular_cotizacion(1000, 0, 10, 19)

    def test_rechaza_porcentaje_fuera_de_rango(self):
        with self.assertRaises(ValueError):
            calcular_cotizacion(1000, 1, 101, 19)


if __name__ == "__main__":
    unittest.main()
