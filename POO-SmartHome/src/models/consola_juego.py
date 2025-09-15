from .dispositivo import Dispositivo

class ConsolaDeJuego(Dispositivo):
    def __init__(self, id, nombre, tipo, marca, estado, idUsuario, automatizaciones):
        super().__init__(id, nombre, tipo, marca, estado, idUsuario, automatizaciones)
        self.almacenamiento = 500  # en GB

    def iniciar_juego_fav(self, juego):
        if self.estado == "encendido":
            print(f"Iniciando el juego {juego} en la consola {self.marca} {self.modelo}.")
        else:
            print("La consola está apagada. No se puede iniciar el juego.")
    