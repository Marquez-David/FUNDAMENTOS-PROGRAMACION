"""

    Nombre: Encima del Umbral.
    OBJ: Determina si una serie de medidas estan por encima de un limite.
    PRE: Los valoresintroducidos deben ser numeros.

"""

def encima_umbral():

    """ Nada --> Nada
    OBJ: Programa que determina los valores pr encima de un limite.
    PRE: Los datos introducidos deben ser numericos. """

    contador_encima = 0

    try :
    
        umbral = float(input("Umbral: "))

        for i in range(5):

            numero = float(input("Numero: "))

            if ( numero > umbral ):

                contador_encima += 1

    except:

        print("Debes introducir valores numericos. ")

    print("Mediciones por encima: " , contador_encima)

encima_umbral()

        

        

        
