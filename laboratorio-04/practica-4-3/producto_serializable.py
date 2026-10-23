import json


class Producto:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def a_diccionario(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(datos["codigo"], datos["nombre"])


if __name__ == "__main__":
    producto = Producto("P001", "Teclado")
    texto_json = json.dumps(producto.a_diccionario(), ensure_ascii=False)
    print("Serializado:", texto_json)

    datos = json.loads(texto_json)
    reconstruido = Producto.desde_diccionario(datos)
    print("Reconstruido:", type(reconstruido), reconstruido.codigo, reconstruido.nombre)
