from App.components.afin import Afin
from App.components.columnas import Columnas
from App.components.vernam import Vernam
from App.services.io import IO

def menu_opciones():
    print(f"\nOpciones\n\t\
            1) Cifrar archivo\n\t\
            2) Descifrar archivo\n\t\
            *) Salir")
        
    opcion = input("Introduzca opción: ")
    return opcion

def menu_cifrados():
    print(f"\nCifrado\n\t\
            1) Afín\n\t\
            2) Columnas\n\t\
            3) Vernam\n\t\
            *) Salir")
        
    opcion = input("Introduzca opción: ")
    return opcion

def desea_guardar():
    print(f"\n¿Desea guardar resultado?\t")
    opcion = input("[1) Sí / *) No]: ")

def main():
    io = IO()
    afin = Afin(a=2, b=3, n=27)
    columnas = Columnas(columnas=3)
    vernam = Vernam()

    print("*****************************************************")
    print("Proyecto de Criptografía - Equipo 11")
    print("Grupo 3 - Prof.ª: Ing. Magdalena Reyes Granados")
    print(f"\nIntegrantes:\
        \nNombres")
    print("*****************************************************")

    while True:
        opcion = menu_opciones()

        if opcion == '1':
            cripto = ""
            print(f"\nCifrado de archivo\n")
            while True:
                archivo = io.abrir_archivo()
                if archivo:
                    break
            contenido = io.archivo_a_cadena(archivo)
            print(f"\nEl mensaje en claro es: \n{contenido}")
            
            '''
            Se solicitó cifrar de manera secuencial,
            sin posibilidad de que el usuario elija
            
            Descomentar código para activar menú

            cifrado = menu_cifrados()
            
            if cifrado == '1':
                cripto = afin.cifrar(contenido)
            elif cifrado == '2':
                cripto = columnas.cifrar(contenido)
            elif cifrado == '3':
                cripto = vernam.cifrar(contenido)
            
            print(f"\nEl mensaje cifrado es: \n{cripto}")

            if cripto != "":
                if desea_guardar():
                    io.guardar_cadena(cripto)

            '''

            ''''''
            print("Introduzca parámetros para Cifrado Afín")

            a = input("a: ")
            b = input("b: ")
            n = input("n [26) Alfabeto inglés 27) Alfabeto español]: ")

            cols = input("Introduzca número de columnas para Cifrado por Columnas: ")

            k = input("Introduzca llave para cifrado Vernam: ")

            afin.set_a(a)
            afin.set_b(b)
            afin.set_n(n)

            columnas.set_columnas(cols)

            vernam.set_k(k)

            cripto = vernam.cifrar(columnas.cifrar(afin.cifrar))
            print(f"\nEl mensaje cifrado es: \n{cripto}")

            while True:
                guardado = io.guardar_cadena(cripto)
                if guardado:
                    break
            
            ''''''

        elif opcion == '2':
            mcla = ""
            print(f"\nDescifrado de archivo\n")
            while True:
                archivo = io.abrir_archivo()
                if archivo:
                    break
            contenido = io.archivo_a_cadena(archivo)
            print(f"\nEl mensaje cifrado es: \n{contenido}")

            '''
            Se solicitó descifrar de manera secuencial,
            sin posibilidad de que el usuario elija
            
            Descomentar código para activar menú

            cifrado = menu_cifrados()
            
            if cifrado == '1':
                mcla = afin.descifrar(contenido)
            elif cifrado == '2':
                mcla = columnas.descifrar(contenido)
            elif cifrado == '3':
                mcla = vernam.descifrar(contenido)
            
            print(f"\nEl mensaje descifrado es: \n{mcla}")

            if mcla != "":
                if desea_guardar():
                    io.guardar_cadena(mcla)

            '''

            ''''''
            print("Introduzca parámetros para Cifrado Afín")

            a = input("a: ")
            b = input("b: ")
            n = input("n [26) Alfabeto inglés 27) Alfabeto español]: ")

            cols = input("Introduzca número de columnas para Cifrado por Columnas: ")

            k = input("Introduzca llave para cifrado Vernam: ")

            afin.set_a(a)
            afin.set_b(b)
            afin.set_n(n)

            columnas.set_columnas(cols)

            vernam.set_k(k)

            mcla = afin.descifrar(columnas.descifrar(vernam.descifrar()))
            print(f"\nEl mensaje descifrado es: \n{mcla}")

            while True:
                guardado = io.guardar_cadena(mcla)
                if guardado:
                    break
            
            ''''''

        else:
            print(f"\nTerminando ejecución\n")
            break
        

    

if __name__ == "__main__":
    main()
