class Afin(object):
    def __init__(self, a=1, b=0, n=27):
        self._a = a
        self._b = b
        self._n = n

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def get_n(self):
        return self._n

    def set_a(self, a):
        self._a = a
    
    def set_b(self, b):
        self._b = b

    def set_n(self, n):
        self._n = n

    def cifrar(self, cadena):
        pass

    def descifrar(self, cadena):
        pass
