"""
****************************************************************************
* Nombre: correccion_test.py                                               *
* OBJ: Corrige un examen tipo test.                                        *
****************************************************************************
"""

def plantilla():

    """  Nada --> list
    OBJ: Crear una lista con las rspuestas correctas.
    PRE: Opciones de respuesta: A-B-C-D-E. """

    lista_plantilla = []

    for respuesta in range(10):

        n = str(input("Respuesta Plantilla: "))

        lista_plantilla.append(n)

    return lista_plantilla

def examen():

    """ Nada --> list
    OBJ: Crear una lista con las respuestas del examinado.
    PRE: Opciones de respuesta: A-B-C-D-E. """

    lista_examen = []

    for respuesta in range(10):

        n = str(input("Respuesta Examinado: "))

        lista_examen.append(n)

    return lista_examen

def comprobacion(lista_plantilla,lista_examen):

    """ list,list --> bool
    OBJ: Determina si un examen tiene fallos.
    PRE: Nada ."""

    fallo = False

    cont = 0

    while(fallo == False and cont <= 9 ):

        if(lista_plantilla[cont] != lista_examen[cont]):

            fallo = True

        else:

            cont += 1

    return fallo

lista_plantilla = plantilla()
lista_examen = examen()
comprobacion(lista_plantilla,lista_examen)

        
