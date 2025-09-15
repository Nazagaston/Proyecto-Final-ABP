import pytest  
from src.models.automatizacion import Automatizacion

def test_agregar_automatizacion():
    automatizacion = Automatizacion(1, "Encender Manana", "06:00", "encender todos", None)
    assert automatizacion.id == 1
    assert automatizacion.nombre == "Encender Manana"
    assert automatizacion.hora == "06:00"
    assert automatizacion.nombre_accion == "encender todos"
    assert automatizacion.dispositivos is None

def test_mostrar_detalles_automatizacion():
    dispositivos = []

    automatizacion = Automatizacion(1, "Encender Manana", "06:00", "encender todos", None)
    detalles = automatizacion.mostrarDetalles()
    assert detalles == "ID: 1, Nombre: Encender Manana, Hora: 06:00, Acción: encender todos, Dispositivos: Ninguno"

#python -m pytest Test/test_automatizacion.py -v