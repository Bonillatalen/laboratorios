class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, group_id):
        # Corrección: Llamada a super() para inicializar self.name en la clase base
        super().__init__(name)
        self.group_id = group_id


student = Student("Carlos", "G-101")
print("Nombre verificado:", student.name)
print("Grupo verificado:", student.group_id)
