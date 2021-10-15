class Afin(object):
    def __init__(self, a=1, b=0, n=27):
        self._a = int(a)
        self._b = int(b)
        self._n = int(n)
        if self._n == 27:
            self._alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        elif self._n == 26:
            self._alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        else:
            print(f"\n[ERROR] No se reconoce tamaño de alfabeto válido.\n")


    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def get_n(self):
        return self._n

    def set_a(self, a):
        self._a = int(a)
    
    def set_b(self, b):
        self._b = int(b)

    def set_n(self, n):
        self._n = int(n)

    def cifrar(self, cadena):
        cripto = ""
        cripto_i = ""
        # Cifrado: Cripto = (Mi*a + b) mod n 

        #Obteniendo los parámetros
        #print("Introduzca parámetros para Cifrado Afín:")

        #a = input("\na: ")
        #b = input("b: ")
        #print("Se usa el alfabeto español de 27 caracteres")
        #n = input("\nTamaño del alfabeto a usar: \n\n26)Alfabeto inglés\n27)Alfabeto español \n\n n: ")


        #Leyendo el mensaje en claro (cadena)
        for indice in range(len(cadena)):
            caracter = cadena[indice]
            caracter = caracter.upper()
            #print("\nEn el indice {} tenemos a '{}'".format(indice, caracter))
            
            #Obteniendo Mi (equivalente con el alfabeto)
            if caracter == " ":
                cripto_i = " "
            else:
                for posicion in range(len(self._alfabeto)):
                    if (caracter == self._alfabeto[posicion]):
                        #print("{} = {}".format(mi, posicion))

                        num = int(posicion)

                        #Cálculo de Ci = (Mi*a + b) mod n

                        #Se castea para convertir los parámetros recibidos (str) a int

                        #a = int(a)
                        #b = int(b)

                        ci = ((num*self._a + self._b) % self._n)
                        #print("ci = ", ci)

                        #Obteniendo Ci a su equivalente para obtener el Cripto 
                        cripto_i = self._alfabeto[ci]
            cripto += cripto_i
        print("\nEl mensaje cifrado es: ",cripto)
        return cripto

    def descifrar(self, cadena):
        mcla = ""
        mcla_i = ""
        # Descifrado: Mi = [(Ci - b) * a^(-1)] mod n 

        # Se obtiene el valor de a^(-1)
        # n = m*a + r1
        m = self._n // self._a
        # 27 // 5 = 5
        r1 = self._n % self._a
        # 27 % 5 = 2
        # 2 = 27 - 5*5 ... (I)

        # a = n*r1 + r2
        n = self._a // r1
        # 5 // 2 = 2
        r2 = self._a % r1
        # 5 % 2 = 1
        # 5 = 2*2 + 1
        # 1 = 5 - 2 * 2 ... (II)
        # (I) en (II)
        # 1 = 5 - 2 * (27 - 5*5)
        # 1 = 5(1 + (-2)(-5)) - 26
        a_inversa = 1 + (n*m)
        #a_inversa = a_inversa / r2
        # 
        
        #print("Introduzca parámetros para Cifrado Afín:")

        #a = input("\na: ")
        #b = input("b: ")
        #print("Se usa el alfabeto español de 27 caracteres")
        #n = input("\nTamaño del alfabeto a usar: \n\n26)Alfabeto inglés\n27)Alfabeto español \n\n n: ")


        #Leyendo el mensaje cifrado (cadena)
        for indice in range(len(cadena)):
            caracter = cadena[indice]
            caracter = caracter.upper()
            #print("\nEn el indice {} tenemos a '{}'".format(indice, caracter))
            
            #Obteniendo Mi (equivalente con el alfabeto)
            if caracter == " ":
                mcla_i = " "
            else:
                for posicion in range(len(self._alfabeto)):
                    if (caracter == self._alfabeto[posicion]):
                        #print("{} = {}".format(mi, posicion))

                        num = int(posicion)

                        #Cálculo de Ci = (Mi*a + b) mod n

                        #Se castea para convertir los parámetros recibidos (str) a int

                        #a = int(a)
                        #b = int(b)

                        mi = (((num - self._b) * a_inversa) % self._n)
                        #print("mi = ", mi)

                        #Obteniendo mi a su equivalente para obtener el Mcla 
                        mcla_i = self._alfabeto[mi]
            mcla += mcla_i
        print("\nEl mensaje descifrado es: ",mcla)
        return mcla
