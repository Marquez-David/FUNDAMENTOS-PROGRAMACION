"""

    Nombre: Suma de los N pares.
    OBJ: Suma los N numeros pares de N hacia delante
"""

def suma_N_pares(N):

    """ int --> Nada
    OBJ: Suma los N pares de N hacia delante
    """

    acumulador = 0

    contador = 0

    for i in range(N*2):

        if ( N%2 == 0):

            acumulador += N

            print(N)

        N += 1

    print("Resultado: ",acumulador)

suma_N_pares(int(input("Numero: ")))
