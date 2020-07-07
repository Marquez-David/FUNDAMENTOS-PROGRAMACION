"""
**************************************************************************
* Nombre: media_master.py                                                *
* OBJ: calcula la media de notas.                                        *
**************************************************************************
"""

def media_master():

    """ Nada --> Float
    OBJ: Calcula la media de una serie de notas.
    PRE: 0 <= notas <= 10 """

    suma = 0

    for n in range(10):

        nota = float(input("Introduce tu nota: "))

        suma += nota

    media = suma / 10

    print(media)

media_master()

        
