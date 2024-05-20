def agregar_libro(biblioteca, titulo, autor):
    # Verificar si el libro ya existe en la biblioteca
    if titulo in biblioteca:
        biblioteca[titulo] += 1
    else:
        # Si no existe, agregarlo con cantidad inicial de 1
        biblioteca[titulo] = 1

# Ejemplo de uso:
biblioteca = {}  # Crear una biblioteca vacía
agregar_libro(biblioteca, "Cien años de soledad", "Gabriel García Márquez")
agregar_libro(biblioteca, "Don Quijote", "Miguel de Cervantes")
print(biblioteca)
