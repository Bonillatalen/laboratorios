class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre


class Instructor(Empleado):
    def __init__(self, nombre, especialidad):
        super().__init__(nombre)
        self.especialidad = especialidad


if __name__ == "__main__":
    instructor = Instructor("Ana", "Python")
    print("Nombre:", instructor.nombre)
    print("Especialidad:", instructor.especialidad)
