class IO(object):

    def abrir_archivo(self):
        '''
        Wrapper para apertura de archivo
        '''
        ruta = input("Introduzca nombre del archivo: ")
        try:
            archivo = open(ruta)
        except IOError:
            print(f"\n[ERROR] No se ha encontrado el archivo {ruta}.\n")
        else:
            print(f"\n[OK] Archivo {ruta} abierto con éxito.\n")
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
            print(f"\n[ERROR] No se pudo leer el archivo {archivo.name}.\n")
        else:
            print(f"\n[OK] Archivo {archivo.name} leído con éxito\n")
            return cadena


    def guardar_cadena(self, cadena):
        '''
        Wrapper para escritura de archivo
        '''
        ruta = input("Introduzca nombre del archivo a guardar: ")
        try:
            with open(ruta, 'w') as f:
                f.write(cadena)
        except IOError:
            print(f"\n[ERROR] El archivo {ruta} se encuentra abierto o no se puede escribir.\n")
        else:
            print(f"\n[OK] Archivo {ruta} guardado con éxito\n")
            return True

        

