class Vernam(object):
    def __init__(self, k = "contrasena"):
        self._k = k

    def get_k(self):
        return self._k

    def set_k(self, k):
        self._k = k

    def cifrar(self, cadena):
        # Se inicializa el criptograma como una cadena vacía
        cripto = ""
        # Se usa un contador para recorrer la llave
        i = 0
        # Se recorre la cadena a cifrar caracter por caracter
        for c in cadena:
            # Se va añadiendo al criptograma el resultado de aplicar
            # la operación XOR (^) entre los códigos ASCII, calculados
            # con ord(), de cada caracter de la cadena y llave. Este resultado
            # se convierte a un caracter antes de agregarse al criptograma.
            cripto += chr(ord(c) ^ ord(self._k[ i % len(self._k)]))
            # Se suma uno al contador que recorre la llave
            i += 1
        # Se regresa el criptograma
        return cripto

    def descifrar(self, cadena):
        # Se inicializa el mensaje en claro como una cadena vacía
        mcla = ""
        # Se usa un contador para recorrer la llave
        i = 0
        # Se recorre la cadena a descifrar caracter por caracter
        for c in cadena:
            # Se va añadiendo al criptograma el resultado de aplicar
            # la operación XOR (^) entre los códigos ASCII, calculados
            # con ord(), de cada caracter de la cadena y llave. Este resultado
            # se convierte a un caracter antes de agregarse al criptograma.
            mcla += chr(ord(c) ^ ord(self._k[ i % len(self._k)]))
            # Se suma uno al contador que recorre la llave
            i += 1
        # Se regresa el mensaje descifrado
        return mcla
