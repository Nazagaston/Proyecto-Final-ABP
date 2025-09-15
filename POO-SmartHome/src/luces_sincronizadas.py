from .dispositivo import Dispositivo

class LucesSincronizadas(Dispositivo):
    def __init__(self, id, nombre, tipo, marca, estado, idUsuario, automatizaciones, color):
        super().__init__(id, nombre, tipo, marca, estado, idUsuario, automatizaciones)
        self.color = color

    def cambiar_color(self, nuevo_color):
        if self.estado == "encendido":
            self.color = nuevo_color
            print(f"Color cambiado a {self.color}.")
        else:
            print("Las luces están apagadas. No se puede cambiar el color.")