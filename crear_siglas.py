"""
*******************************************************************************
* Nombre: crear_siglas.py
* OBJ: A partir de una frase, crea sus siglas.
*******************************************************************************
"""

def crear_siglas(organismo):

    """ str > str
    OBJ: Crear siglas a partir de una frase.
    PRE: La frase debe estar bien escrita. """

    siglas = ''

    organismo = organismo.strip().split(' ')

    for palabra in organismo:

        if(palabra[0] == palabra[0].upper() and (len(palabra) >= 4) ):

            siglas += palabra[0]

        if(palabra[len(palabra)-1] == 's'):

            siglas += palabra[0]

    return siglas

print(crear_siglas('Futbol Club Barcelona'))

        

        
