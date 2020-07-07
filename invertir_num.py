"""
******************************************************************************
* Nombre: invertir_num.py
* OBJ: Invertir numero cualquiera.
******************************************************************************
"""

def invertir(num):

    """ int -> Nada
    OBJ: Invertir numero.
    PRE: num debe ser int. """

    #Procedimiento: no encuentro ningun uso fuera de este programa

    num_invert = 0

    while num>0: 

        num_invert = num_invert*10+num%10

        num = num//10

    return num_invert

#Probador
invertir(1234567)
