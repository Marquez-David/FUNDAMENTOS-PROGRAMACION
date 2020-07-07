"""
****************************************************************************
* Nombre: es_capicua.py
* OBJ: Si un numero es capicua.
****************************************************************************
"""

from invertir_num import invertir

def es_capicua(num):

    """ int -> bool
    OBJ: Si un numero es capicua.
    PRE: num > 0. """

    capicua = False

    num_invertido = invertir(num)

    if(num_invertido == num):

        capicua = True

    return capicua

#Probador
print(es_capicua(313))
