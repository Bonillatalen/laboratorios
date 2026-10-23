
unidades_disponibles = 12
unidades_solicitadas = 15

hay_suficientes = unidades_disponibles >= unidades_solicitadas
cantidades_iguales = unidades_disponibles == unidades_solicitadas
solicitaron_mas = unidades_solicitadas > unidades_disponibles

print("¿Hay suficientes unidades?", hay_suficientes)
print("¿Las cantidades son iguales?", cantidades_iguales)
print("¿Se solicitaron más unidades?", solicitaron_mas)