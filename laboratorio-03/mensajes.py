# ==========================================
# Archivo: mensajes.py
# Práctica: Funciones, parámetros y argumentos
# ==========================================

# 1. Funciones sin parámetros para estructura de mensajes
def mostrar_encabezado():
    print("============================")
    print("        SALUDO PYTHON       ")
    print("============================")

def mostrar_despedida():
    print("============================")
    print("        ADIÓS PYTHON        ")
    print("============================")


# 2. Funciones con parámetros
def saludar(nombre):
    print(f"Hola, {nombre}")

def mostrar_producto(nombre, cantidad):
    print(f"Producto: {nombre}")
    print(f"Existencias: {cantidad}")

def presentar(nombre, ciudad):
    print(f"{nombre} vive en {ciudad}")

mostrar_encabezado()


saludar("Laura")
saludar("Andrés")


print("\n--- Inventario ---")
mostrar_producto("Teclado", 4)
mostrar_producto("Mouse", 7)


mostrar_encabezado()


print("--- Presentaciones (Posicionales) ---")
presentar("Ana", "Bogotá")
presentar("Cali", "Luis") 

print("\n--- Presentación Corregida (Nombrados) ---")
presentar(ciudad="Cali", nombre="Luis")


mostrar_despedida()