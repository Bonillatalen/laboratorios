"""Cotizador de compra del Laboratorio 01."""


def calcular_cotizacion(precio_unitario, cantidad, porcentaje_descuento,
                        porcentaje_impuesto, costo_envio=1000.0):
    """Calcula subtotal, descuento, impuesto y total de una cotización."""
    if precio_unitario < 0:
        raise ValueError("El precio unitario no puede ser negativo")
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que cero")
    if not 0 <= porcentaje_descuento <= 100:
        raise ValueError("El descuento debe estar entre 0 y 100")
    if not 0 <= porcentaje_impuesto <= 100:
        raise ValueError("El impuesto debe estar entre 0 y 100")
    if costo_envio < 0:
        raise ValueError("El costo de envío no puede ser negativo")

    subtotal = precio_unitario * cantidad
    valor_descuento = subtotal * (porcentaje_descuento / 100)
    base_descuento = subtotal - valor_descuento
    valor_impuesto = base_descuento * (porcentaje_impuesto / 100)
    total = base_descuento + valor_impuesto + costo_envio
    return {
        "subtotal": subtotal,
        "valor_descuento": valor_descuento,
        "base_descuento": base_descuento,
        "valor_impuesto": valor_impuesto,
        "costo_envio": costo_envio,
        "total": total,
    }


def solicitar_datos():
    """Solicita datos al usuario y devuelve los valores de la cotización."""
    nombre = input("Ingrese su nombre: ").strip()
    producto = input("Ingrese el nombre del producto: ").strip()
    precio_unitario = float(input("Ingrese el precio unitario del producto: "))
    cantidad = int(input("Ingrese la cantidad de productos: "))
    porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
    porcentaje_impuesto = float(input("Ingrese el porcentaje de impuesto: "))
    nombre_vendedor = input("Ingrese el nombre del vendedor: ").strip()
    codigo_cotizacion = input("Ingrese el código de cotización: ").strip()
    datos = calcular_cotizacion(precio_unitario, cantidad,
                                porcentaje_descuento, porcentaje_impuesto)
    return nombre, producto, nombre_vendedor, codigo_cotizacion, datos


def main():
    try:
        nombre, producto, vendedor, codigo, datos = solicitar_datos()
        print(f"\nCliente: {nombre}")
        print(f"Producto: {producto}")
        print(f"Subtotal: $ {datos['subtotal']:.2f}")
        print(f"Descuento: $ {datos['valor_descuento']:.2f}")
        print(f"Impuesto: $ {datos['valor_impuesto']:.2f}")
        print(f"Costo de envío: $ {datos['costo_envio']:.2f}")
        print(f"Nombre del vendedor: {vendedor}")
        print(f"Código de cotización: {codigo}")
        print(f"Total: $ {datos['total']:.2f}")
    except (ValueError, TypeError) as error:
        print(f"Entrada no válida: {error}")
        print("Revise que los valores numéricos sean correctos e intente de nuevo.")


if __name__ == "__main__":
    main()
