"""
***************************************************************************
* Nombre: pos_1_aparicion.py
* OBJ: Posicion de la primer aparicion de un elem en tupla.
***************************************************************************
"""

def pos_aparicion(tupla,elem):

    """ tupla --> int
    OBJ: Primera aparicion de un elemento en una tupla
    PRE: La tupla debe tener  elementos. """

    esta = False

    tamT = len(tupla)

    pos = 0

    while (not(esta) and pos<tamT):

        if(tupla[pos]==elem):

            esta = True

        pos += 1

    if(not(esta)):

        pos = -1

    return pos
        
#Probador
dias_semana = ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes')
dia = 'Sabado'
print(pos_aparicion(dias_semana, dia))
    
