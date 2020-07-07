"""

    Nombre: Es serie limpia
    OBJ: Determinar si una serie es limpia.

"""

def serie_limpia():

    """ nada --> bool
    OBJ: Determinar si una serie es limpia.
    """

    CENTINELA = -9999

    serie_limpia = True

    numero_anterior = 0 

    numero_serie = int(input("Numero(-9999para terminar): "))

    cuantos_numeros = 1 #Cuenta cuantos numeros tiene la serie.

    elem_central = numero_serie

    posicion_elem_central = -1

    while ( numero_serie != CENTINELA and serie_limpia ):

        if( numero_serie != numero_anterior):

            elem_central = numero_serie

            posicion_elem_central = cuantos_numeros

        if ( cuantos_numeros == 1):

            serie_limpia = True

        elif( cuantos_numeros % 2 == 0 and numero_serie == numero_anterior):

            serie_limpia == True

        elif(numero_anterior == numero_serie and elem_central < numero_serie ):

             serie_limpia == True
            
        else:

            serie_limpia = False

        numero_anterior = numero_serie

        numero_serie = int(input("Numero(-9999 para terminar): "))

        cuantos_numeros += 1
            
if (serie_limpia()):

    print("La serie es limpia. ")

else:

    print("La serie no es limpia. ")
