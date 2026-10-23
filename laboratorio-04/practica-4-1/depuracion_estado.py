# Corrección: Validar antes de mutar el estado
nueva_cantidad = -5

if nueva_cantidad < 0:
    print("Cantidad inválida. La operación fue rechazada sin alterar el objeto.")
else:
    # Solo se asigna si pasa la verificación
    # producto._cantidad = nueva_cantidad
    pass
