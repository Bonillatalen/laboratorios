
calificaciones = [4.5, 3.2, 5.0, 3.2, 4.0, 2.8]

print("Tres primeras calificaciones:", calificaciones[:3])
print("Dos últimas calificaciones:", calificaciones[-2:])
print("Cantidad total:", len(calificaciones))

ordenadas = sorted(calificaciones)
print("Calificaciones ordenadas:", ordenadas)

nota = 3.2
print(f"La nota {nota} aparece {calificaciones.count(nota)} veces.")

print("Lista original:", calificaciones)
