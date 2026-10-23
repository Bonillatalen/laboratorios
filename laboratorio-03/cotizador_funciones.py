
def calcular_subtotal(precio, cantidad):
    return precio * cantidad


def calcular_descuento(subtotal, porcentaje):
    return subtotal * (porcentaje / 100)


def calcular_impuesto(base, porcentaje):
    return base * (porcentaje / 100)


precio = 100000
cantidad = 2
descuento_porcentaje = 10
impuesto_porcentaje = 19


subtotal = calcular_subtotal(precio, cantidad)
descuento = calcular_descuento(subtotal, descuento_porcentaje)
base_despues_descuento = subtotal - descuento
impuesto = calcular_impuesto(base_despues_descuento, impuesto_porcentaje)
total = base_despues_descuento + impuesto


print(f"Subtotal: {int(subtotal)}")
print(f"Descuento: {int(descuento)}")
print(f"Base después del descuento: {int(base_despues_descuento)}")
print(f"Impuesto: {int(impuesto)}")
print(f"Total: {int(total)}")