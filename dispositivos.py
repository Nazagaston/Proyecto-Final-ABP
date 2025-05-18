dispositivos = []

def agregar_dispositivo():
    nombre = input("Nombre del dispositivo: ")
    print("\nTipo de dispositivo")
    print("1. Consola de juego")
    print("2. Equipo de sonido")
    print("3. Television")
    print("4. Luces Sincronizadas")
    opcion = input("Seleccione una opción:")

    if opcion == '1':
        tipo = "consola_de_juego"
    elif opcion == '2':
        tipo = "equipo_de_sonido"
    elif opcion == '3':
       tipo = "television"
    elif opcion == '4':
        tipo = "luces_sincronizadas"
    marca= input("Marca:")
    estado= input("Estado (Encendido/Apagado):")

    dispositivo = {
        "nombre": nombre,
        "tipo": tipo,
        "estado": estado,
        "marca": marca,
    }

    # Campos específicos por tipo
    if tipo == "luces_sincronizadas":
        color = input("Color de la luz: ")
        dispositivo["color"] = color
    elif tipo == "equipo_de_sonido":
        potencia = input("Potencia (W): ")
        dispositivo["potencia"] = potencia
    elif tipo == "television":
        tamaño = input("Tamaño (pulgadas): ")
        dispositivo["tamaño"] = tamaño
   
    dispositivos.append(dispositivo)
    print(f"Dispositivo '{nombre}' agregado.")

def listar_dispositivos():
    if not dispositivos:
        print("No hay dispositivos registrados.")
        return
    for indice, valor in enumerate(dispositivos, 1):
        extra = ""
        for clave in valor:
            if clave not in ["nombre", "tipo", "estado" ]:
                extra += f" | {clave}: {valor[clave]}"
        print(f"{indice}. {valor['nombre']} ({valor['tipo']}) - {valor['estado']}{extra}")

def buscar_dispositivo():
    nombre = input("Ingrese el nombre a buscar: ")
    for d in dispositivos:
        if d["nombre"] == nombre:
            print(f"{d['nombre']} ({d['tipo']}) - {d['estado']}")
            return
    print("Dispositivo no encontrado.")

def eliminar_dispositivo():
    nombre = input("Ingrese el nombre del dispositivo a eliminar: ")
    for d in dispositivos:
        if d["nombre"] == nombre:
            dispositivos.remove(d)
            print("Dispositivo eliminado.")
            return
    print("No se encontró el dispositivo.")