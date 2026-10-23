class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo)
        self.cilindraje = cilindraje


if __name__ == "__main__":
    moto1 = Motocicleta("Yamaha", "MT-07", 689)
    moto2 = Motocicleta("KTM", "Duke 390", 373)
    print(f"Moto 1: {moto1.marca} {moto1.modelo} - {moto1.cilindraje}cc")
    print(f"Moto 2: {moto2.marca} {moto2.modelo} - {moto2.cilindraje}cc")
