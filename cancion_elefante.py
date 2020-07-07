"""

    Nombre: Generar versos de cancion.
    OBJ: Programa que genera el verso de una cancion en concreto.

"""

def generar_versos(numero_elef):

    """ int --> Nada
    OBJ: Generar tantos vesos de una cancion como el usuario indique.
    """

    i = 1

    if(numero_elef < 0):

        print("Numero de elefantes debe ser mayor que 0. ")

    else:
        
        while( i <= numero_elef):

            if ( i == 1 ):
            
                print( i , " Elefante se baalanceaba sobre la tela de ..." )
            
            else:

                print( i , " Elefantes se balanceaban sobre la tela de ...")

            i += 1
            
try:
    
    generar_versos(int(input("Cuantos elefantes: ")))

except ValueError:

    print("Numero  introducido invalido. ")

