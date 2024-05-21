import pickle

# Ejemplo de una lista de transacciones
lista_transacciones = [
    {"monto": 100, "fecha": "2024-05-20", "descripcion": "Compra en tienda", "tipo": "Gasto"},
    {"monto": 50, "fecha": "2024-05-21", "descripcion": "Pago de factura", "tipo": "Gasto"},
    # Agrega más transacciones aquí...
]

# Guardar la lista en un archivo llamado 'datos_financieros.pkl'
with open('datos_financieros.pkl', 'wb') as archivo:
    pickle.dump(lista_transacciones, archivo)

print("Datos guardados correctamente.")
