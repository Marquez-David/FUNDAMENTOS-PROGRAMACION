"""
    Nombre: Creciente_ decreciente_desordenados
    OBJ: Determina el orden de una serie de numeros.
"""

def orden_serie():

    """Nada --> Nada
    OBJ: Determina elorden de una serie.
    """
    
    num = int(input("Numero: "))

    num_anterior = 9999
    num_anterior2 = -9999

    creciente = 0
    decreciente = 0
    desordenada = 0
    
    for i in range(10):

        if( num < num_anterior2):

            decreciente += 1

        elif(num > num_anterior):

            creciente+= 1

        elif( num == num_anterior):

            desordenada += 1

        num_anterior = num
        num_anterior2 = num

        try:
        
            num = int(input("Numero: "))

        except ValueError:

            print("Introduzca numeros validos. ")

    if ( creciente == 9): print("Creciente")
    elif(decreciente == 9): print("Decreciente")
    elif(desordenada > 0 and desordenada < 9): print("Desordenada")

orden_serie()

        
        


        
