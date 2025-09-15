class Automatizacion:
    def __init__(self, id, nombre,hora, nombre_accion, dispositivos):
        self.id = id
        self.nombre = nombre
        self.hora = hora
        self.nombre_accion = nombre_accion
        self.dispositivos = dispositivos

    def ejecutar(self):
        if self.condicion():
            self.accion()

    def mostrarDetalles(self):
        dispositivos_nombres = [dispositivo.nombre for dispositivo in self.dispositivos] if self.dispositivos else ["Ninguno"]
        return f"ID: {self.id}, Nombre: {self.nombre}, Hora: {self.hora}, Acción: {self.nombre_accion}, Dispositivos: {', '.join(dispositivos_nombres)}"
