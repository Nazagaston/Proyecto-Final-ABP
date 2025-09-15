class GestorDispositivos:
    def __init__(self):
        self.dispositivos = []

    def agregar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)

    def eliminar_dispositivo(self, dispositivo):
        if dispositivo in self.dispositivos:
            self.dispositivos.remove(dispositivo)

    def buscar_dispositivo(self, nombre):
        for dispositivo in self.dispositivos:
            if dispositivo.nombre == nombre:
                return dispositivo
        return None

    def listar_dispositivos(self):
        for dispositivo in self.dispositivos:
            print(f"{dispositivo.nombre} - {dispositivo.tipo} - {dispositivo.estado}")