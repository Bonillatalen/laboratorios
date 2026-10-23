notas = [2.5, 3.8, 4.1]

estados = ["Aprobado" if nota >= 3.0 else "No aprobado" for nota in notas]

print(estados)