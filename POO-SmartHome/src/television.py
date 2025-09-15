from .dispositivo import Dispositivo

class Television (Dispositivo):
    def __init__(self, id, nombre, tipo, marca, estado, idUsuario, automatizaciones, tamano):
        super().__init__(id, nombre, tipo, marca, estado, idUsuario, automatizaciones)
        self.tamano = tamano
        self.hdmi = 1 
      

    def encender(self):
        if self.estado != "encendido":
            self.estado = "encendido"
            print(f"La televisión {self.marca} {self.modelo} está encendida.")
        else:
            print(f"La televisión {self.marca} {self.modelo} ya está encendida.")

    def apagar(self):
        if self.encendida:
            self.encendida = False
            print(f"La televisión {self.marca} {self.modelo} está apagada.")
        else:
            print(f"La televisión {self.marca} {self.modelo} ya está apagada.")

    def cambiar_hdmi(self, nuevo_hdmi):
        if self.estado == "encendido":
            if nuevo_hdmi > 0:
                self.hdmi = nuevo_hdmi
                print(f"HDMI cambiado a {self.hdmi}.")
            else:
                print("El HDMI debe ser un número positivo.")
        else:
            print("La televisión está apagada. No se puede cambiar de HDMI.")

