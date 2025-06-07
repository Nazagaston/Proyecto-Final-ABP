from datos import dispositivos, automatizaciones

def agregar_dispositivo():
    nombre_dispositivo = input("Nombre del dispositivo: ")

    while True:
        print("\nTipo de dispositivo")
        print("1. Consola de juego")
        print("2. Equipo de sonido")
        print("3. Televisión")
        print("4. Luces Sincronizadas")
        opcion_tipo_dispositivo = input("Seleccione una opción: ")

        if opcion_tipo_dispositivo == '1':
            tipo_dispositivo = "consola_de_juego"
            break
        elif opcion_tipo_dispositivo == '2':
            tipo_dispositivo = "equipo_de_sonido"
            break
        elif opcion_tipo_dispositivo == '3':
            tipo_dispositivo = "television"
            break
        elif opcion_tipo_dispositivo == '4':
            tipo_dispositivo = "luces_sincronizadas"
            break
        else:
            print("Opción inválida. Intentá nuevamente.")

    marca_dispositivo = input("Marca: ")

    # Validación del estado del dispositivo
    while True:
        estado_dispositivo = input("Estado (Encendido/Apagado): ")
        if estado_dispositivo.lower() == "encendido":
            estado_dispositivo = "Encendido"
            break
        elif estado_dispositivo.lower() == "apagado":
            estado_dispositivo = "Apagado"
            break
        else:
            print("Estado inválido. Solo se permite 'Encendido' o 'Apagado'.")

    nuevo_dispositivo = {
        "id": len(dispositivos) + 1,
        "nombre": nombre_dispositivo,
        "tipo": tipo_dispositivo,
        "estado": estado_dispositivo,
        "marca": marca_dispositivo
    }

  
    if tipo_dispositivo == "luces_sincronizadas":
        color_luz = input("Color de la luz: ")
        nuevo_dispositivo["color"] = color_luz
    elif tipo_dispositivo == "equipo_de_sonido":
        potencia_sonido = input("Potencia (W): ")
        nuevo_dispositivo["potencia"] = potencia_sonido
    elif tipo_dispositivo == "television":
        tamaño_pantalla = input("Tamaño (pulgadas): ")
        nuevo_dispositivo["tamaño"] = tamaño_pantalla

    dispositivos.append(nuevo_dispositivo)
    print(f"Dispositivo '{nombre_dispositivo}' agregado correctamente.")

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

    __all__ = ["dispositivos", "agregar_dispositivo", "listar_dispositivos", "buscar_dispositivo", "eliminar_dispositivo"]
