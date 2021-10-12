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
    afin = Afin()
    columnas = Columnas()
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
            
            cifrado = menu_cifrados()
            
            if cifrado == '1':
                cripto = afin.cifrar(contenido)
            elif cifrado == '2':
                cripto = columnas.cifrar(contenido)
            elif cifrado == '3':
                cripto = vernam.cifrar(contenido)

            if cripto != "":
                if desea_guardar():
                    io.guardar_cadena(cripto)

        elif opcion == '2':
            mcla = ""
            print(f"\nDescifrado de archivo\n")
            while True:
                archivo = io.abrir_archivo()
                if archivo:
                    break
            contenido = io.archivo_a_cadena(archivo)
            
            cifrado = menu_cifrados()
            
            if cifrado == '1':
                mcla = afin.descifrar(contenido)
            elif cifrado == '2':
                mcla = columnas.descifrar(contenido)
            elif cifrado == '3':
                mcla = vernam.descifrar(contenido)
            
            if mcla != "":
                if desea_guardar():
                    io.guardar_cadena(mcla)

        else:
            print(f"\nTerminando ejecución\n")
            break
        

    

if __name__ == "__main__":
    main()
