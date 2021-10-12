from App.components.afin import Afin
from App.components.columnas import Columnas
from App.components.vernam import Vernam
from App.services.io import IO

def main():
    io = IO()
    print("*****************************************************")
    print("Proyecto de Criptografía - Equipo 11")
    print("Grupo 3 - Prof.ª: Ing. Magdalena Reyes Granados")
    print(f"\nIntegrantes:\
        \nNombres")
    print("*****************************************************")

    while True:
        print(f"\nOpciones\n\t\
            1) Cifrar archivo\n\t\
            2) Descifrar archivo\n\t\
            *) Salir")
        
        opcion = input("Introduzca opción: ")

        if opcion == '1':
            print(f"\nCifrado de archivo\n")
            while True:
                archivo = io.abrir_archivo()
                if archivo:
                    break
        elif opcion == '2':
            print(f"\nDescifrado de archivo\n")
            while True:
                archivo = io.abrir_archivo()
                if archivo:
                    break
        else:
            print(f"\nTerminando ejecución\n")
            break
        

    

if __name__ == "__main__":
    main()
