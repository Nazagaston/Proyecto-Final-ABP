from dispositivos import dispositivos
from datetime import datetime

def ejecutar_automatizacion():
    hora_actual = datetime.now().strftime("%H:%M")
    if hora_actual == "07:00":
        print("Ejecutando automatización: Encendiendo todos los dispositivos a las 7:00 AM...")
        for d in dispositivos:
            d["estado"] = "Encendido"
        print("Todos los dispositivos han sido encendidos.")
    else:
        print(f"No es hora de automatización. Hora actual: {hora_actual}. Debe ser 07:00.")