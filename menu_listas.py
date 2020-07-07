"""
***************************************************************************
* Nombre: menu_opciones.py                                                *
* OBJ: Realiza la opcion que el usuario desee.                            *
***************************************************************************
"""

def menu_pantalla():

    """ Nada --> Nada
    OBJ: Realiza la opcion que el usuario desee.
    PRE: 0 <= opcion <= 4. """

    print("Opcion 0: El programa finalza. ")
    print("Opcion 1: Ordena una lista de mayor a menor. ")
    print("Opcion 2: Dada una lista determina el mayor y menor numero. ")
    print("Opcion 3: Media aritmetica de una lista. ")
    print("Opcion 4: Darla vuleta a una lista. ")

    opcion = int(input("Que opcion deseas: "))

    if(opcion == 0):

        print("FIN DEL PRORAMA. ")

    elif(opcion == 1):

        print(menor_a_mayor(lista_num))

    elif(opcion == 2):

        print("El mayor numero es: ", mayor(lista_num))

        print("El menor numero es: ", menor(lista_num))

    elif(opcion == 3):

        print("La media aritmetica es: ", media_aritmetica(lista_num))

    elif(opcion == 4):

       print("La lista dada la vuelte es: ", dar_vuelta(lista_num))

    else:

        print("La opcion elegida es invalida")


def mayor(lista_num):

    """ lista --> int
    OBJ: Determinar el numero mayor de una lista.
    PRE: Nada. """

    mayor = -999999999

    for num in lista_num:

        if(num > mayor):

            mayor = num

    return mayor

def menor(lista_num):

    """ lista --> int
    OBJ: Determina el menor  numero de una lista.
    PRE: Nada. """

    menor = 99999999999

    for num in lista_num:

        if(num < menor):

            menor = num

    return menor

def media_aritmetica(lista_num):

    """ lista --> float
    OBJ: Calcula la media aritmetica de elementos de una lista.
    PRE: Nada. """

    media = 0.0

    for num in lista_num:

        media += num

    media = media / len(lista_num)

    return media

def dar_vuelta(lista_num):

    """ lista --> lista
    OBJ: Dar la vuleta a una lista.
    PRE: Nada. """

    lista_del_reves = []

    for i in range(len(lista_num)-1,-1,-1):

        lista_del_reves.append(lista_num[i])

    return lista_del_reves

def menor_a_mayor(lista_num):

    """ lista --> lista
    OBJ: Ordena una lista de menor a mayor.
    PRE: Nada. """

    lista_orden = []

    lista_aux = lista_num

    for i in range(len(lista_aux)):

        num_menor = menor(lista_aux)

        lista_orden.append(num_menor)

        lista_aux.remove(num_menor)

    return lista_orden


lista_num = [4,9,3,16,6,4,9,7,69]


menu_pantalla()





















        
