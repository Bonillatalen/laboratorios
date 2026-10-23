nombre = "Alejandro"
salario = 820000.0
cantidad_horas = 3
porcentaje_descuento = 0.04


subtotal = cantidad_horas * salario
valor_descuento = subtotal * porcentaje_descuento
total = subtotal - valor_descuento

print("Nombre:", nombre)
print("Salario por hora: $", salario)
print("Cantidad de horas:", cantidad_horas)
print("Subtotal: $", subtotal)
print("Descuento: $", valor_descuento)
print("Total: $", total)