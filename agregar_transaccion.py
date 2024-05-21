def agregar_transaccion(lista_transacciones, monto, fecha, descripcion, tipo):
    # Crear un diccionario con los datos de la transacción
    transaccion = {
        "monto": monto,
        "fecha": fecha,
        "descripcion": descripcion,
        "tipo": tipo
    }
    # Agregar la transacción a la lista
    lista_transacciones.append(transaccion)

# Ejemplo de uso:
lista_transacciones = []  # Crear una lista vacía para almacenar transacciones
agregar_transaccion(lista_transacciones, 100, "2024-05-20", "Compra en tienda", "Gasto")
print(lista_transacciones)
