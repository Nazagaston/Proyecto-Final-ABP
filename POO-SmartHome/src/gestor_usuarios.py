class GestorUsuarios:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def iniciar_sesion(self, email, contrasena):
        for usuario in self.usuarios:
            if usuario.email == email and usuario.contrasena == contrasena:
                return usuario
        return None
    
    def modificar_rol(self, usuario, nuevo_rol):
        usuario.rol = nuevo_rol

    def eliminar_usuario(self, usuario):
        self.usuarios.remove(usuario)

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario.verDatosusuario())