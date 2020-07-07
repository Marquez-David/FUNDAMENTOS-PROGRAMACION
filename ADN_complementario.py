"""
*******************************************************************************
* Nombre: ADN_complementario.py
* OBJ: Crear una cadena de ADN complementario A-T, G-C.
*******************************************************************************
"""


def crear_complementario(ADN):

    """ sttr -> str
    OBJ: ADN complementario  A->T, G->C.
    PRE: Cadena de ADN valida. """

    ADN_comp = ''

    for molecula in ADN:

        if(molecula == 'A'):

            ADN_comp += 'T'

        elif(molecula == 'T'):

            ADN_comp += 'A'

        elif(molecula == 'G'):

            ADN_comp += 'C'

        elif(molecula == 'C'):

            ADN_comp += 'G'

    return ADN_comp

print(crear_complementario('ATCGTAAGATACGT'))
        
