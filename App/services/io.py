class IO(object):

    @classmethod
    def abrir_archivo(ruta):
        '''
        Wrapper para apertura de archivo
        '''
        ruta = input("Introduzca nombre del archivo: ")
        try:
            archivo = open(ruta)
        except IOError:
            print(f"[ERROR] No se ha encontrado el archivo {ruta}.")
        else:
            return archivo
    
    @classmethod
    def archivo_a_cadena(archivo):
        '''
        Extrae el contenido de un objeto File
        '''
        try:
            cadena = ""
            with archivo as f:
                lineas = f.readlines()
            for linea in lineas:
                cadena += linea.rstrip()
        except IOError:
            print(f"[ERROR] No se pudo leer el archivo {archivo.name}.")
        else:
            return cadena


    @classmethod
    def guardar_cadena(ruta, cadena):
        '''
        Wrapper para escritura de archivo
        '''
        try:
            with open(ruta, 'w') as f:
                f.write(cadena)
        except IOError:
            print(f"[ERROR] El archivo {ruta} se encuentra abierto o no se puede escribir.")
        else:
            return True

        

