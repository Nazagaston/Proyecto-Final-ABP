import pytest   
from src.usuario import Usuario

def test_registrar_usuario():
    usuario = Usuario(1, "Nazarena", "nazarena@gmail.com", "1999", "admin")
    assert usuario.idUsuario == 1
    assert usuario.nombre == "Nazarena"
    assert usuario.email == "nazarena@gmail.com"
    assert usuario.contrasena  == "1999"
    assert usuario.rol == "admin"

def test_verDatos_usuario():
    usuario = Usuario(1, "Nazarena", "nazarena@gmail.com", "1999", "admin")
    datos = usuario.verDatosusuario()
    assert datos == f"ID: {usuario.idUsuario}, Nombre: {usuario.nombre}, Email: {usuario.email}, Rol: {usuario.rol}"

def test_conocerRol_usuario():
    usuario = Usuario(1, "Nazarena", "nazarena@gmail.com", "1999", "admin")
    rol = usuario.conocerRol()
    assert rol == "admin"

#python -m pytest Test/test_usuario.py -v