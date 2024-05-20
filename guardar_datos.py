#importamos pickle
import pickle
#guardamos los datos en el archivo
def guardar_datos(biblioteca):
    with open("datos_biblioteca.pkl", "wb") as archivo:
        pickle.dump(biblioteca, archivo)
    print("Datos guardados correctamente.")


biblioteca = {
    "Cien años de soledad": ("Gabriel García Márquez", 3, True),
    "Don Quijote": ("Miguel de Cervantes", 1, False)
}
guardar_datos(biblioteca)



