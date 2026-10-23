class Notificacion:
    def enviar(self):
        return "Enviando notificación general"


class Correo(Notificacion):
    def enviar(self):
        return "Enviando correo electrónico"


class MensajeTexto(Notificacion):
    def enviar(self):
        return "Enviando mensaje de texto"


if __name__ == "__main__":
    notificaciones = [Notificacion(), Correo(), MensajeTexto()]
    for notificacion in notificaciones:
        print(notificacion.enviar())
