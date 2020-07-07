"""

    Nombre: Cuantos_pares_impares.
    OBJ: Programa que determina cuantos pares e impares.

"""

def calculo_pares_impares():

    """ Nada --> Nada
    OBJ: Detrmian cuantos pares e impares.
    """

    CENTINELA = -9999

    contador_pares = 0

    contador_impares = 0

    numero = int(input("Numero: "))

    while ( numero != CENTINELA):

        if ( numero % 2 == 0):

            contador_pares += 1

        else :

            contador_impares += 1

        numero = int(input("Numero: "))

    print("Pares: ", contador_pares , "Impares: " , contador_impares)

calculo_pares_impares()
