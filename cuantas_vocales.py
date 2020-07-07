"""
***************************************************************************
* Nombre: cuantas_vocales.py                                              *
* OBJ: Cuenta las vocales que hay en una palabra.                         *
***************************************************************************
"""

def cuantas_vocales(palbr):

    """ str --> int, int, int, int ,int
    OBJ: Cuantas vocales tiene una palabra.
    PRE: Nada """

    cont_a = 0
    cont_e = 0
    cont_i = 0
    cont_o = 0
    cont_u = 0
    

    for letra in palbr:

        if(letra == 'a'):

            cont_a += 1

        elif(letra == 'e'):

            cont_e += 1

        elif(letra == 'i'):

            cont_i += 1

        elif(letra == 'o'):

            cont_o += 1

        elif(letra == 'u'):

            cont_u += 1
            

    return cont_a,cont_e,cont_i,cont_o,cont_u

cuantas_vocales(str(input("Palabra: ")))
