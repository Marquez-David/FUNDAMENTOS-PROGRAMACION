"""

    Nombre: Media_Mayor_Menor
    OBJ: Calcula lamedia,elmayor y elmenor de una serie de numeros.
    PRE: El usuario debe introducir numeros.

"""

CENTINELA = -9999

cuantos_numeros = 0

acumulador = 0

elem_mayor = -99999999

elem_menor = 999999999

numero = float(input("Numero(-9999 para terminar): "))

while ( numero != CENTINELA):

    #Calcular media:

    acumulador += numero

    cuantos_numeros += 1

    resultado = acumulador / cuantos_numeros

    #Calcula mayor
    
    if( numero > elem_mayor):

        elem_mayor = numero

    #Calcula menor

    if(numero < elem_menor):

        elem_menor = numero

    numero = float(input("Numero(-9999 para terminar): "))

print("Media: ", resultado)

print("Menor: ", elem_menor)

print("Mayor: ", elem_mayor)
    










    
