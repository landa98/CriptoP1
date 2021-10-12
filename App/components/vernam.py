class Vernam(object):
    def __init__(self, k = "contrasena"):
        self._k = k

    def get_k(self):
        return self._k

    def set_k(self, k):
        self._k = k

    def cifrar(self, cadena):
        pass

    def descifrar(self, cadena):
        pass
