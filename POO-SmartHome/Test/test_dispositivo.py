import pytest
from src.models.dispositivo import Dispositivo
from src.models.television import Television
from src.models.luces_sincronizadas import LucesSincronizadas

def test_crear_Television():
    dispositivo = Television(0,"TV salon","Television", "Samsung","apagado",1, None, "40 pulgadas")
    assert dispositivo.id == 0
    assert dispositivo.nombre == "TV salon"
    assert dispositivo.tipo == "Television"
    assert dispositivo.marca == "Samsung"
    assert dispositivo.estado == "apagado"
    assert dispositivo.idUsuario == 1
    assert dispositivo.automatizaciones is None
    assert dispositivo.tamano == "40 pulgadas"

def test_crear_LucesSincronizadas():
    dispositivo = LucesSincronizadas(1,"Luces LED","Luces", "Philips","apagado",1, None, "blanco")
    assert dispositivo.id == 1
    assert dispositivo.nombre == "Luces LED"
    assert dispositivo.tipo == "Luces"
    assert dispositivo.marca == "Philips"
    assert dispositivo.estado == "apagado"
    assert dispositivo.idUsuario == 1
    assert dispositivo.automatizaciones is None
    assert dispositivo.color == "blanco"

def test_encender_apagar_dispositivo():
    dispositivo = Dispositivo(0,"TV salon","Television", "Samsung","apagado",1, None)
    dispositivo.encender()
    assert dispositivo.estado == "encendido"
    dispositivo.apagar()
    assert dispositivo.estado == "apagado"

#python -m pytest Test/test_dispositivo.py -v