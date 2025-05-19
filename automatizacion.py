from datetime import datetime
from dispositivos import dispositivos

automatizaciones = []

def crear_automatizacion():
    nombre = input("Nombre de la automatización: ")
    hora = input("Hora programada (formato HH:MM): ")
    accion = input("Acción (por ahora: 'encender todos'): ")

    if accion != "encender todos":
        print("Por ahora solo se permite la acción: 'encender todos'")
        return

    nueva = {
        "id": len(automatizaciones) + 1,
        "nombre": nombre,
        "hora": hora,
        "accion": accion
    }

    automatizaciones.append(nueva)
    print("Automatización creada con éxito.")

def listar_automatizaciones():
    if not automatizaciones:
        print("No hay automatizaciones registradas.")
        return

    print("\n--- Automatizaciones ---")
    for a in automatizaciones:
        print(f"{a['id']}. {a['nombre']} - {a['hora']} - {a['accion']}")

def eliminar_automatizacion():
    if not automatizaciones:
        return

    id_a_borrar = int(input("Ingrese el ID de la automatización a eliminar: "))
    for a in automatizaciones:
        if a["id"] == id_a_borrar:
            automatizaciones.remove(a)
            print("Automatización eliminada.")
            return
    print("No se encontró la automatización.")
   