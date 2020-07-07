"""
****************************************************************************
* Nombre: cad_inv_impar.py                                                 *
* OBJ: Imprime una cad inversa a partir de los eleme impares de otra.      *
****************************************************************************
"""

def cad_impar(cad):

    """ str --> str
    OBJ: Devuelve una cadena con los elemimpares de otra.
    PRE: Nada ."""

    cad2 = cad.split(' ')

    lista_cadena = []

    cont = 0

    for palabra in cad2:

        if ((cont % 2) == 0):

            lista_cadena.append(palabra)

        cont += 1

    return lista_cadena

def invertir_lista(lista_cad):

    """ list --> str
    OBJ: Devuelve una cadena invertida
    PRE: Nada. """

    lista_invertida = []

    cad_final = ''

    for i in lista_cad[::-1]:

        lista_invertida.append(i)

    cad_final = ' '.join(lista_invertida)

    return cad_final


cad = 'estoy demostrando que se programar en python'

lista_cad = cad_impar(cad)

invertir_lista(lista_cad)
