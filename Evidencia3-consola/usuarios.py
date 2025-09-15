lista_usuarios = []

def registrar_usuario():
    print("\n--- Registro de Usuario ---")
    
    nombre_completo = input("Nombre completo: ")
    correo_electronico = input("Correo electrónico: ")
    contraseña_usuario = input("Contraseña: ")
    
    rol_usuario = "admin" if len(lista_usuarios) == 0 else "usuario"

    nuevo_usuario = {
        "nombre": nombre_completo,
        "correo": correo_electronico,
        "contraseña": contraseña_usuario,
        "rol": rol_usuario
    }

    lista_usuarios.append(nuevo_usuario)
    print(f"Usuario registrado exitosamente como '{rol_usuario}'.")

def iniciar_sesion():
    print("\n--- Inicio de Sesión ---")
    
    correo_ingresado = input("Correo: ")
    contraseña_ingresada = input("Contraseña: ")

    for usuario_en_lista in lista_usuarios:
        if (usuario_en_lista["correo"] == correo_ingresado and
                usuario_en_lista["contraseña"] == contraseña_ingresada):
            print(f"Sesión iniciada como {usuario_en_lista['rol'].capitalize()}")
            return usuario_en_lista

    print("Credenciales incorrectas.")
    return None

def modificar_rol_usuario():
    correo_objetivo = input("Correo del usuario cuyo rol querés modificar: ")
    
    for usuario_en_lista in lista_usuarios:
        if usuario_en_lista["correo"] == correo_objetivo:
            nuevo_rol = input("Nuevo rol (admin/usuario): ").lower()
            if nuevo_rol in ["admin", "usuario"]:
                usuario_en_lista["rol"] = nuevo_rol
                print("Rol actualizado correctamente.")
            else:
                print("Rol inválido. Solo se permite 'admin' o 'usuario'.")
            return

    print("Usuario no encontrado.")

def mostrar_datos_usuario(usuario_logueado):
    print("\n--- Mis Datos ---")
    print(f"Nombre: {usuario_logueado['nombre']}")
    print(f"Correo: {usuario_logueado['correo']}")
    print(f"Rol: {usuario_logueado['rol']}")