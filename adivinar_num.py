"""
*****************************************************************************
* Nombre: adivinar_num.py
* OBJ: El usuario introduce numeros hasta que adivine unnum premiado.
*****************************************************************************
"""

def num_premiado(premiado):

    """ Nada -> Nada
    OBJ: Pide numeros al usuario hasta que acierta en num premiado
    PRE: Nada. """

    centi = -9999

    intentos = 0

    def entero_pedido(): #Encapsulamiento de funciones

        """ Nada -> int
        OBJ: No errores en la introduccion de datos. """

        try: num = int(input('Numero(-9999 para terminar): '))

        except: num = 0

        return num

    num = entero_pedido()

    while (num != centi and num!= premiado):

        intentos += 1

        num = entero_pedido()

    print('Intentos: ', intentos)

#Probador
premiado = 123
num_premiado(premiado)

        

        
