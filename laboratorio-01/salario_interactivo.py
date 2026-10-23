nombre = input("Escribe tu nombre: ")
horas_trabajadas =int(input("Ingrese la cantidad de horas trabajadas: "))
valor_hora = float(input("Ingrese el valor por hora: "))

salario = horas_trabajadas * valor_hora
print(nombre, "tu salario es: $", salario)