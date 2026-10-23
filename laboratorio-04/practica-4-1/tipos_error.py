try:
    cantidad = int("abc")
except ValueError:
    print("ValueError: El contenido no representa un entero.")

try:
    cantidad = int(None)
except TypeError:
    print("TypeError: El tipo recibido no permite esa conversión.")
