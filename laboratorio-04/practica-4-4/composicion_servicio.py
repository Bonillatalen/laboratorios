class Almacenamiento:
    def guardar(self, datos):
        print(f"[Almacenamiento] Guardando {len(datos)} registros de forma persistente.")


class ServicioInventario:
    def __init__(self, almacenamiento):
        self.almacenamiento = almacenamiento

    def guardar_inventario(self, productos):
        self.almacenamiento.guardar(productos)


if __name__ == "__main__":
    servicio = ServicioInventario(Almacenamiento())
    servicio.guardar_inventario(["Teclado", "Mouse", "Monitor"])
