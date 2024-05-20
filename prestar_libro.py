def prestar_libro(biblioteca, titulo, usuario):
    # Verificar si el libro está en la biblioteca
    if titulo in biblioteca:
        autor, cantidad, disponible = biblioteca[titulo]
        if disponible:
            # El libro está disponible, prestarlo al usuario
            biblioteca[titulo] = (autor, cantidad - 1, False)
            print(f"Libro prestado: {titulo} a {usuario}")
        else:
            print(f"El libro {titulo} no está disponible actualmente.")
    else:
        print(f"El libro {titulo} no existe en la biblioteca.")

# Ejemplo de uso:
biblioteca = {
    "Cien años de soledad": ("Gabriel García Márquez", 3, True),
    "Don Quijote": ("Miguel de Cervantes", 1, False)
}
prestar_libro(biblioteca, "Cien años de soledad", "Usuario123")
