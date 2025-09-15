from .dispositivo import Dispositivo    

class Computadora(Dispositivo):
    def __init__(self, id, nombre, tipo, marca, estado, idUsuario, automatizaciones, procesador):
        super().__init__(id, nombre, tipo, marca, estado, idUsuario, automatizaciones)
        self.procesador = procesador

    def abrir_programa_fav(self, programa):
        if self.estado == "encendido":
            print(f"Abriendo el programa {programa} en la computadora {self.marca}.")
        else:
            print("La computadora está apagada. No se puede abrir el programa.")

    