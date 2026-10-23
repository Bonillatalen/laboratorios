# Corrección: Se reemplaza ZeroDivisionError por ValueError
try:
    numero = int("hola")
except ValueError:
    print("No se pudo convertir: cadena no convertible a entero.")
