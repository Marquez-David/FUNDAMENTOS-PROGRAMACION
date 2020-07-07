"""
    Nombre: Total de positivos y negativos.
    OBJ: Calcula cuantos positivos y negativos introduc el usurio.
    PRE: Los valores introducidos deben ser enteros.

"""

def numero_positivos_negativos():

    CENTINELA = -9999
    positivos = 0
    negativos = 0
    ceros = 0

    numero = int(input("Numero: "))
    
    while( numero != CENTINELA ):

        if(numero>0):

            positivos += 1

        elif(numero < 0 ):

            negativos += 1

        else :

            ceros += 1

        numero = int(input("Numero: "))

    print("Negativos: ", negativos ,"Positivos: ",positivos,"Ceros: ", ceros)

numero_positivos_negativos()
