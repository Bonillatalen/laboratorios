class Notificacion:
    def enviar(self, mensaje):
        raise NotImplementedError("Las subclases deben implementar enviar()")


class NotificacionCorreo(Notificacion):
    def enviar(self, mensaje):
        return f"[CORREO] Despachando a SMTP: {mensaje}"


class NotificacionConsola(Notificacion):
    def enviar(self, mensaje):
        return f"[CONSOLA] Salida estándar: {mensaje}"


if __name__ == "__main__":
    notificadores = [NotificacionCorreo(), NotificacionConsola()]
    for n in notificadores:
        print(n.enviar("Alerta de stock bajo"))
