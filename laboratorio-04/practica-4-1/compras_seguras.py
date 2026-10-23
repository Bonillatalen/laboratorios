compras_aceptadas = 0
total_acumulado = 0.0

print("--- Registro de Compras (0 para terminar) ---")
while True:
    entrada = input("Importe de compra: ")
    try:
        importe = float(entrada)
    except ValueError:
        print("Rechazado: La entrada debe ser un número convertible.")
        continue

    if importe == 0:
        break

    if importe < 0:
        print("Rechazado: El importe no puede ser negativo.")
        continue

    compras_aceptadas += 1
    total_acumulado += importe
    print(f"Compra registrada: ${importe:.2f}")

print("\n--- Resumen Final ---")
print(f"Compras aceptadas: {compras_aceptadas}")
print(f"Suma acumulada: ${total_acumulado:.2f}")
