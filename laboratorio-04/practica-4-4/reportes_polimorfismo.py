class ReporteTexto:
    def generar(self, datos):
        return f"Reporte Detallado: Contenido total -> {', '.join(datos)}"


class ReporteResumen:
    def generar(self, datos):
        return f"Reporte Resumen: Total de elementos registrados -> {len(datos)}"


if __name__ == "__main__":
    elementos = ["Servidor", "Base de Datos", "API Gateway"]
    generadores = [ReporteTexto(), ReporteResumen()]

    for gen in generadores:
        print(gen.generar(elementos))
