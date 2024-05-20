def registrar_usuario(biblioteca, nombre, identificacion):
    # Verificar si el usuario ya está registrado
    if identificacion in biblioteca:
        print(f"El usuario {nombre} ya está registrado.")
    else:
        # Agregar al usuario a la biblioteca
        biblioteca[identificacion] = nombre
        print(f"Usuario {nombre} registrado con éxito.")

# Ejemplo de uso:
usuarios = {}  # Crear un diccionario para almacenar usuarios
registrar_usuario(usuarios, "Juan Pérez", "123456")
