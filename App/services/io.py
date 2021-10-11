class IO(object):
    def __init__(self):
        ruta = input("Introduzca nombre del archivo: ")
        try:
            archivo = open(ruta)
        except IOError:
            print(f"[EROR] No se ha encontrado el archivo {ruta}."
