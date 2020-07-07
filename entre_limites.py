"""
*******************************************************************************
* Nombre: entre_limites.py
* OBJ: Pide al usuario un numero entre un rango.
*******************************************************************************
"""

def limites(mini,maxi,msg):

    """ int, int, int, str --> int
    OBJ: Pide un numero al usuario hasta que mini<=num<=maxi. """

    def entero_pedido(mini,maxi,msg): #Subprograma encapsulado

        """ int, int, str -> int
        OBJ: Corrige la posibilidad de error de valor. """

        try: num = int(input('Numero (min:%d, max:%d): ' %(mini,maxi)))

        except ValueError: num = maxi+1 #Forzamos la entrada al bucle

        return num

    def real_pedido(mini,maxi,msg):

        """ int, int -> float
        OBJ: Corrige la posibilidad de eeror de valor. """

        try: num = float(input('Numero (min:%d, max:%d): ' %(mini,maxi)))

        except ValueError: num = maxi+1

        return num

    num = entero_pedido(mini,maxi,msg)

    while( not(mini<=num<=maxi) ):

        print(msg)

        num = entero_pedido(mini,maxi,msg)

    return num

#Probador

#mensaje = 'Error: Introduce otro numero'

#limites(10, 20, mensaje)
