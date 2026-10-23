try:
    num1 = float(input("Dividendo: "))
    num2 = float(input("Divisor: "))
    resultado = num1 / num2
except ValueError:
    print("Error: Debe ingresar valores numéricos válidos.")
except ZeroDivisionError:
    print("Error: No es posible dividir entre cero.")
else:
    print(f"Resultado de la división: {resultado}")
