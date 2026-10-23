
total = 0
contador = 0

deposito = int(input("Depósito (0 para terminar): "))

while deposito != 0:
    if deposito > 0:
        total = total + deposito
        contador = contador + 1
        print(f"Ahorro acumulado: {total}")
    else:
        print("El depósito debe ser positivo.")

    print()
    deposito = int(input("Depósito (0 para terminar): "))

print()
print(f"Depósitos válidos: {contador}")
print(f"Total ahorrado: {total}")
