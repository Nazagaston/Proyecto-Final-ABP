class Dispositivo:
    def __init__(self, id, nombre, tipo, marca,estado,idUsuario,automatizaciones):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.marca = marca
        self.estado = estado
        self.idUsuario = idUsuario
        self.automatizaciones = automatizaciones

    def encender(self):
        self.estado = "encendido"

    def apagar(self):
        self.estado = "apagado"

    def obtenerEstado(self):
        return self.estado
    
    def agregarAutomatizacion(self, automatizacion):
        self.automatizaciones.append(automatizacion)

    def eliminarAutomatizacion(self, automatizacion):
        if automatizacion in self.automatizaciones:
            self.automatizaciones.remove(automatizacion)
    
    def listarAutomatizaciones(self):
        return self.automatizaciones
    
    def ejecutarAutomatizacion(self, automatizacion):
        if automatizacion in self.automatizaciones:
            automatizacion.ejecutar()  