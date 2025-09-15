class Usuario:
    def __init__(self, idUsuario, nombre, email, contrasena, rol):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.email = email
        self.contrasena = contrasena
        self.rol = rol

    def verDatosusuario(self):
        return f"ID: {self.idUsuario}, Nombre: {self.nombre}, Email: {self.email}, Rol: {self.rol}"

    def conocerRol(self):
        return self.rol 
