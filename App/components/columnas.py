class Columnas(object):
    def __init__(self, columnas = "clave", mcla = "este es un mensaje de prueba"):
        self._columnas = columnas
        self._mcla = mcla

    def get_columnas(self):
        return self._columnas

    def get_mcla(self):
        return self._mcla

    def set_columnas(self, columnas):
        self._columnas = columnas

    def set_mcla(self, mcla):
        self._mcla = mcla    

    def cifrar(self, cadena, mcla):
        long_cadena=len(cadena)
        long_mcla=len(mcla)
        Lista_aux=[]
        aux=int(long_mcla/long_cadena)+1
        for i in range(aux):
            Lista_aux.append([])
        for i in range(aux):
            for j in range(long_cadena):
                if long_mcla>(i*long_cadena)+j:
                    Lista_aux[i].append(mcla[(i*long_cadena)+j])
                else:
                    Lista_aux[i].append('x')
        print(Lista_aux)
        cripto=''
        lista_trans_cif=transpuesta(Lista_aux)
        print(lista_trans_cif)
        cadena_sort = sorted(cadena)
        lista_trans_cif2=[]
        for i in range(long_cadena):
            indice=cadena.index(cadena_sort[i])
            lista_trans_cif2.append(lista_trans_cif[indice])
        print(lista_trans_cif2)    
        lista_cif=transpuesta(lista_trans_cif2)
        print(lista_cif)
        cripto=reconstruccion(lista_cif)
        print(cripto)
        return cripto

    def descifrar(self, cadena):
        mcla = cadena
        return mcla

    '''
    def transpuesta(self, lista):
        long_hor=len(lista[0])
        long_ver=len(lista)
        lista_trans=[]
        for i in range(long_hor):
            for j in range(long_ver):
                lista_trans[i][j].append(lista[j][i])
        return lista_trans   '''

    

def transpuesta(lista):
    long_hor=len(lista[0])
    long_ver=len(lista)
    lista_trans=[]
    for i in range(long_hor):
            lista_trans.append([])
    for i in range(long_hor):
        for j in range(long_ver):
            lista_trans[i].append(lista[j][i])
    return lista_trans 

def reconstruccion(lista_rec):
    long_hor=len(lista_rec[0])
    long_ver=len(lista_rec)
    palabra=''
    for i in range(long_ver):
        for j in range(long_hor):
            palabra=palabra+lista_rec[i][j]
    return palabra



