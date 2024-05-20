def mostrar_libros(biblioteca):
    for titulo, detalles in biblioteca.items():
        autor, cantidad, disponible = detalles
        estado = "Disponible" if disponible else "No disponible"
        print(f"{titulo} - {autor} ({cantidad} unidades, {estado})")

# Ejemplo de uso:
biblioteca = {
    "Cien años de soledad": ("Gabriel García Márquez", 3, True),
    "Don Quijote": ("Miguel de Cervantes", 1, False)
}
mostrar_libros(biblioteca)
