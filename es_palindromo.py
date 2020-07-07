"""
****************************************************************************
* Nombre: es_palindromo.py                                                 *
* OBJ: Determinar si una palabra es palindromo.                            *
****************************************************************************
"""

def es_palindromo(palbr):

    """ str --> bool
    OBJ: Determina si una palabra es palindromo.
    PRE:  Nada """

    lista_palabra = [] #Reservamos memoria para la lista de palabra

    palind = True

    cont = 0

    for letra in palbr: #Meter la palabra en una lista

        lista_palabra.append(letra)

    print(lista_palabra)

    for letra in range (len(lista_palabra)//2): #Recorre la mitad de la lista

        cont -= 1

        if(lista_palabra[letra] != lista_palabra[cont]):

           palind = False

    print(palind)

    return palind

es_palindromo("anitalagordalagartonanotragaladrogalatina")
