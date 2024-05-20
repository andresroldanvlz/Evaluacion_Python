#importamos pickle 
import pickle
#cargamos los datos
def cargar_datos():
    try:
        with open("datos_biblioteca.pkl", "rb") as archivo:
            biblioteca = pickle.load(archivo)
            print("Datos cargados correctamente.")
            return biblioteca
    except FileNotFoundError:
        print("El archivo no existe. Inicializando biblioteca vacía.")
        return {}


biblioteca_cargada = cargar_datos()