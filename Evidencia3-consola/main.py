from usuarios import (
    registrar_usuario,
    iniciar_sesion,
    mostrar_datos_usuario,
    modificar_rol_usuario,
    lista_usuarios
)
from dispositivos import (
    agregar_dispositivo,
    listar_dispositivos,
    buscar_dispositivo,
    eliminar_dispositivo
)
from automatizacion import (
    crear_automatizacion,
    listar_automatizaciones,
    eliminar_automatizacion,
    ejecutar_automatizacion
)

def menu_usuario(usuario_logueado):
    while True:
        print("\n--- Menú Usuario ---")
        print("1. Consultar mis datos")
        print("2. Gestionar mis dispositivos")
        print("3. Ejecutar automatización")
        print("4. Crear automatización")
        print("5. Eliminar automatización")
        print("0. Cerrar sesión")
        opcion_usuario = input("Seleccione una opción: ")

        if opcion_usuario == '1':
            mostrar_datos_usuario(usuario_logueado)
        elif opcion_usuario == '2':
            menu_gestion_dispositivos()
        elif opcion_usuario == '3':
            ejecutar_automatizacion()
        elif opcion_usuario == '4':
            crear_automatizacion()
        elif opcion_usuario == '5':
            eliminar_automatizacion()
        elif opcion_usuario == '0':
            print("Sesión cerrada.")
            break
        else:
            print("Opción inválida.")

def menu_admin(usuario_logueado):
    while True:
        print("\n--- Menú Admin ---")
        print("1. Consultar automatizaciones activas")
        print("2. Crear automatización")
        print("3. Eliminar automatización")
        print("4. Gestionar dispositivos")
        print("5. Modificar rol de usuario")
        print("0. Cerrar sesión")
        opcion_admin = input("Seleccione una opción: ")

        if opcion_admin == '1':
            listar_automatizaciones()
        elif opcion_admin == '2':
            crear_automatizacion()
        elif opcion_admin == '3':
            eliminar_automatizacion()
        elif opcion_admin == '4':
            menu_gestion_dispositivos()
        elif opcion_admin == '5':
            modificar_rol_usuario()
        elif opcion_admin == '0':
            print("Sesión cerrada.")
            break
        else:
            print("Opción inválida.")

def menu_gestion_dispositivos():
    while True:
        print("\n--- Gestión de Dispositivos ---")
        print("1. Agregar dispositivo")
        print("2. Listar dispositivos")
        print("3. Buscar dispositivo")
        print("4. Eliminar dispositivo")
        print("0. Volver")
        opcion_dispositivo = input("Seleccione una opción: ")

        if opcion_dispositivo == '1':
            agregar_dispositivo()
        elif opcion_dispositivo == '2':
            listar_dispositivos()
        elif opcion_dispositivo == '3':
            buscar_dispositivo()
        elif opcion_dispositivo == '4':
            eliminar_dispositivo()
        elif opcion_dispositivo == '0':
            break
        else:
            print("Opción inválida.")

def main():
    while True:
        print("\n--- Sistema SmartHome ---")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("0. Salir")
        opcion_inicio = input("Seleccione una opción: ")

        if opcion_inicio == '1':
            registrar_usuario()
        elif opcion_inicio == '2':
            usuario_logueado = iniciar_sesion()
            if usuario_logueado:
                if usuario_logueado['rol'] == 'admin':
                    menu_admin(usuario_logueado)
                else:
                    menu_usuario(usuario_logueado)
        elif opcion_inicio == '0':
            print("Gracias por usar SmartHome. ¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()