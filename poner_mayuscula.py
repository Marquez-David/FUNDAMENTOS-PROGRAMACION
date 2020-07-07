"""
***********************************************************************
* Nombre: poner_mayuscula.py                                          *
* OBJ: Pone en mayuculas todas las primeras letras de una palabra.    *
***********************************************************************
"""

def poner_mayus(lista_frase):

    """ str --> lista
    OBJ: Pone en mayucula todas las primeras letras de una frase.
    PRE: Nada. """

    for i in range(len(lista_frase)):

        if(lista_frase[i] == " "):

            lista_frase[i+1].upper()

    return lista_frase

def meter_en_lista(frase):

    """ str --> lista
    OBJ: Mete la frase en una lista.
    PRE: Nada. """

    lista_frase = []

    lista_frase = list("".join(frase))

    return lista_frase


frase = 'hola maniana tengo examen me quiero cortar los cojones'

lista_frase = meter_en_lista(frase)

print(poner_mayus(lista_frase))
