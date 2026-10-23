def calcular_cobro(valor_compra, envio=10000):
    """Devuelve la suma del valor de compra y el costo de envío."""
    return valor_compra + envio


cobro_estandar = calcular_cobro(50000)

cobro_gratis = calcular_cobro(50000, envio=0)


print(f"Cobro con envío estándar: ${cobro_estandar}")
print(f"Cobro con envío gratuito:  ${cobro_gratis}")