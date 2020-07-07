"""
****************************************************************************
* Nombre: suma_lista.py                                                    *
* OBJ: Sumar dos listas con el mismo numero de eelemtos.                   *
****************************************************************************
"""

def suma_lista(lista1,lista2):

    """ lista, lista --> lista
    OBJ: Suma dos listas.
    PRE: Las listas deben tener la misma longuitud. """

    suma = 0

    lista_suma = []

    for i in range(len(lista1)):

        for j in range(len(lista2)):

            if( j == i ):

                suma = lista1[i] + lista2[j]

                lista_suma.append(suma)

    return lista_suma

def aniadir_elem(lista1,lista2):

    """ lista, lista --> Nada
    OBJ: Suma elementos de listas de distinto tamanio.
    PRE: Las listas deben tener numeros. """

    iguales = False

    separacion = cuanta_separacion(lista1,lista2)

    suma_listas = []

    while(iguales == False):

        if(len(lista1) == len(lista2)):

            iguales = True

        elif(len(lista1) < len(lista2)):

            for i in range(separacion):

                lista1.append(0) #Aniadimos tantos 0 como separacion

        else:

            for j in range(separacion):

                lista2.append(0)

    print(suma_lista(lista1,lista2))


def cuanta_separacion(lista1,lista2):

    """ lista, lista --> int
    OBJ: Determina cuantos elementos tiene de mas una lista que otra.
    PRE: Nada. """

    cont_lista1 = 0

    cont_lista2 = 0

    separacion = 0

    for i in range(len(lista1)):

        cont_lista1 += 1

    for j in range(len(lista2)):

        cont_lista2 += 1

    separacion = abs(cont_lista1 - cont_lista2)

    return separacion


lista1 = [5,8,2,7,1,9,9]

lista2 = [4,1,9,3,5,7,0,5,1,3]

aniadir_elem(lista1,lista2)
