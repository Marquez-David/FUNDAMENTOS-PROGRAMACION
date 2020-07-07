"""
**************************************************************************
* Nombre: dif_conjuntos.py                                               *
* OBJ: Array con elementos Array1, no esten en Array2 sin repeticion.    *
**************************************************************************
"""

def dif_conjuntos(conj1,conj2):

    """ Array, Array --> Array
    OBJ: Devuelve un array con los elemtos de conj1 pero no en conj2.
    PRE: Los arrays deben terner eel mismo tamaño. """

    conj3 = []

    cont = 0 #Cuenta cuantas veces se repite num1 en conj2

    for num1 in conj1:

        cont = 0#Elcntador se reinicia para cda numero

        for num2 in conj2:

            if(num1 == num2):

                cont += 1

        if (cont == 0): #Si elemento no esta en conj2

            conj3.append(num1)

    return conj3

def sin_repeticion(conj3):

    """ Array -> Array
    OBJ: Elimina los elementos repetidos de conj3.
    PRE: Nada. """

    cont = 0#Cuenta cuantas veces se repite un numero en un mismo conjunto

    for num in conj3:

        cont = 0#Reiniciamos el contador para cada numero

        for num2 in conj3:

            if(num == num2):

                cont += 1

        if(cont > 1):#Si aparece mas de una vez

            conj3.remove(num2)

    return conj3

conj1 = [3,6,8,9,1,2,3,3,3]

conj2 = [4,7,1,4,0,8,4]

conj3 = dif_conjuntos(conj1,conj2)

print(sin_repeticion(conj3))
