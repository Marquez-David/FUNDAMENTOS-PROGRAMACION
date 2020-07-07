"""
******************************************************************************
* Nombre: es_dni_valido.py
* OBJ: Si un dni es valido.
*******************************************************************************
"""

LETRAS = ('T','R','W','A','G','M','Y','F','P','D','X','B',
          'N','J','Z','S','Q','V','H','L','C','K','E')

NUMEROS = ('1','2','3','4','5','6','7','8','9')

CONTROL = ('X','Y','Z')

def es_dni(dni,LETRAS,NUMEROS,CONTROL):

    """ str -> bool
    OBJ: Si un dni es valido
    PRE: Nada. """

    valido = True

    nD = len(dni)

    letra = dni[8:9]

    cont = 1

    while valido and cont<(nD-1): #Controlamos los dig del centro sean numeros

        if(dni[cont] not in NUMEROS):

            valido = False

        cont += 1

    if(dni[0] not in NUMEROS and dni[0] not in CONTROL): #El primer digito puede ser xyz o num

        valido = False

    if(nD != 9 and letra not in LETRAS): #La letra debe estar entre las posibles letras

        valido = False

    return valido

def pedir_dni():

    """ str -> Nada
    OBJ: Pide un dni al usuario hasta que introduzca uno valido. """

    dni = str(input('DNI: '))

    while not(es_dni(dni,LETRAS,NUMEROS,CONTROL)):

        print('DNI no valido')

        dni = str(input('DNI: '))


#Probador
#print(es_dni(dni,LETRAS))
pedir_dni()
