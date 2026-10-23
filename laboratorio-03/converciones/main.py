
from unidades import kilometros_a_metros, celsius_a_fahrenheit

print("=== CONVERSOR DE UNIDADES ===")

km = float(input("Ingresa los kilómetros a convertir: "))
metros = kilometros_a_metros(km)
print(f"{km} km equivalen a {metros:,.2f} metros\n")

c = float(input("Ingresa los grados Celsius a convertir: "))
f = celsius_a_fahrenheit(c)
print(f"{c} °C equivalen a {f:.2f} °F")