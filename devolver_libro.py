def devolver_libro(biblioteca, titulo, usuario):
    # Verificar si el libro está en la biblioteca
    if titulo in biblioteca:
        autor, cantidad, disponible = biblioteca[titulo]
        if not disponible:
            # El libro está prestado, devolverlo al usuario
            biblioteca[titulo] = (autor, cantidad + 1, True)
            print(f"Libro devuelto: {titulo} por {usuario}")
        else:
            print(f"El libro {titulo} no está prestado actualmente.")
    else:
        print(f"El libro {titulo} no existe en la biblioteca.")

# Ejemplo de uso:
biblioteca = {
    "Cien años de soledad": ("Gabriel García Márquez", 3, True),
    "Don Quijote": ("Miguel de Cervantes", 1, False)
}
devolver_libro(biblioteca, "Cien años de soledad", "Usuario123")
