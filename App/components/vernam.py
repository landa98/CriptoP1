class Vernam(object):
    def __init__(self, k = "contrasena"):
        self._k = k

    def get_k(self):
        return self._k

    def set_k(self, k):
        self._k = k

    def cifrar(self, cadena):
        cripto = cadena
        return cripto

    def descifrar(self, cadena):
        mcla = cadena
        return mcla
