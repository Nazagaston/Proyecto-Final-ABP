from .dispositivo import Dispositivo

class EquipoDeSonido(Dispositivo):
    def __init__(self, id,nombre, tipo, marca, estado, idUsuario, automatizaciones, potencia):
        super().__init__(id,nombre, tipo, marca, estado, idUsuario, automatizaciones)
        self.potencia = potencia
        self.volumen = 10

    def subir_volumen(self):
        if self.estado == "encendido":
            self.volumen += 1
            print(f"Volumen subido a {self.volumen}.")
        else:
            print("El equipo de sonido está apagado. No se puede subir el volumen.")

    def bajar_volumen(self):
        if self.estado == "encendido":
            self.volumen -= 1
            print(f"Volumen bajado a {self.volumen}.")
        else:
            print("El equipo de sonido está apagado. No se puede bajar el volumen.")
