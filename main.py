
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


def mostrar_menu():
    print("\n--- Menú SmartHome ---")
    print("1. Agregar dispositivo")
    print("2. Listar dispositivos")
    print("3. Buscar dispositivo")
    print("4. Eliminar dispositivo")
    print("5. Ejecutar automatización (Encender todos a las 7:00 AM)")
    print("6. Crear automatización")
    print("7. Listar automatizaciones")
    print("8. Eliminar automatización")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_dispositivo()
        elif opcion == '2':
            listar_dispositivos()
        elif opcion == '3':
            buscar_dispositivo()
        elif opcion == '4':
            eliminar_dispositivo()
        elif opcion == '5':
            ejecutar_automatizacion()    
        elif opcion == '6':
            crear_automatizacion()
        elif opcion == '7':
            listar_automatizaciones()
        elif opcion == '8':
            eliminar_automatizacion()
        elif opcion == '0':
            print("Gracias por usar SmartHome. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()