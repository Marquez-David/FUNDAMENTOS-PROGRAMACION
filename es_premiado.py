"""
***************************************************************************
* Nombre: es_premiado.py                                                  *
* OBJ: Entre los numeros introducidos, esta el premiado y el mas cercano. *
***************************************************************************
"""

def es_premiado(num_premiado):

    """ int --> bool, int, int, int
    OBJ: Si un numeo esta en la serie y el mascercano a el.
    PRE: Los numeros introducidos deben ser enteros. """

    CENTINELA = -9999

    pos_premiado = -1 #Si no se introduce el premiado

    cerc_premiado = 9999

    pos_cerc = -1 # Despues se va ha modificar, simplemente lo inicializo.

    premiado = False

    contador = 0

    n = int(input("Numero(-9999 para terminar): "))

    while(n!=CENTINELA) and not(premiado) :

        if(num_premiado == n):

            contador += 1

            pos_premiado = contador

            premiado = True

        elif(abs(n-num_premiado) < abs(cerc_premiado-num_premiado)):

                contador += 1

                cerc_premiado = n

                pos_cerc = contador

                n = int(input("Numero(-9999 para terminar): "))

        else:

            contador += 1

            n = int(input("Numero(-9999 para terminar): "))

    # Simplemente para visualizar que lo he hecho bien.

    print("es_premiado = ", premiado,"; Posicion premiado: ", pos_premiado)

    print("mas cercano = ", cerc_premiado, "posicio mas cercano = ", pos_cerc)

    return premiado,pos_premiado,cerc_premiado,pos_cerc

#Probador

es_premiado(6)
es_premiado(0)
es_premiado(99)
es_premiado(5)

            

        

            
