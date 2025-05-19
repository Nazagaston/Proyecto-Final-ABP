from datetime import datetime
from datos import dispositivos, automatizaciones


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
        print(f"Id: {a['id']}. Nombre: {a['nombre']} - Hora: {a['hora']} - Accion: {a['accion']}")

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


def ejecutar_automatizacion():
    hora_actual = datetime.now().strftime("%H:%M")
    if not automatizaciones:
        print("No hay automatizaciones registradas.")
        return
    for a in automatizaciones:
        if a["hora"] == hora_actual and a["accion"] == "encender todos":
            print(f"Ejecutando automatización: {a['nombre']} (ID {a['id']})")
            for d in dispositivos:
                d["estado"] = "Encendido"
