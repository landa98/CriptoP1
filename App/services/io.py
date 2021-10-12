class IO(object):

    def abrir_archivo(self):
        '''
        Wrapper para apertura de archivo
        '''
        ruta = input("Introduzca nombre del archivo: ")
        try:
            archivo = open(ruta)
        except IOError:
            print(f"[ERROR] No se ha encontrado el archivo {ruta}.")
        else:
            print(f"[OK] Archivo abierto con éxito.")
            return archivo
    
    def archivo_a_cadena(self, archivo):
        '''
        Extrae el contenido de un objeto File
        '''
        try:
            cadena = ""
            with archivo as f:
                lineas = f.readlines()
            for linea in lineas:
                cadena += linea.rstrip() + "  "
        except IOError:
            print(f"[ERROR] No se pudo leer el archivo {archivo.name}.")
        else:
            return cadena


    def guardar_cadena(self, ruta, cadena):
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

        

