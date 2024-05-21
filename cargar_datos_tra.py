import pickle
import os

def cargar_datos_transacciones(ruta_archivo):
    try:
        with open(ruta_archivo, 'rb') as archivo:
            while True:
                try:
                    yield pickle.load(archivo)
                except EOFError:
                    break
    except FileNotFoundError:
        print("El archivo no existe. Inicializando en un estado vacío.")

# Ejemplo de uso:
archivo_transacciones = 'datos_financieros.pkl'
for transaccion in cargar_datos_transacciones(archivo_transacciones):
    print(transaccion)

# Puedes adaptar este código según tus necesidades específicas.
