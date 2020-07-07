"""
*****************************************************************************************
* Nombre: array_distinto.py                                                             *
* Obj: Devolver Array3 con elementos de Array1, !pertenecen a Array2 sin repeticion.    *
*****************************************************************************************
"""

def crear_array(array1,array2):

    """ array, array --> array
    OBJ: Devolver un array con elem que estan en arra1 y no en array2.
    PRE: Nada """

    array3 = []

    cont = 0

    for elem1 in array1:

        cont = 0 # Reiniciamos el contador con cada elemento.

        for elem2 in array2:

            if (elem2 == elem1 ): 

                cont += 1 # Sumamos 1 al contador cada vez que los elemtos sean iguales

        if( cont == 0): # Si no hay ningun elem = al elem del array1 lo introducimos en array3

            array3.append(elem1)

    return array3

def eliminar_repetido(array3):

    """ array -> array
    OBJ: Elimina los elementos repetidos de un array.
    PRE: Nada """

    array4 = []

    array4 = array3 #Creamos una copia de array

    cont = 0

    for elem1 in array4:

        cont = 0 #Reiniciamos el contador con cada elemento.

        for elem2 in array3:

            if(elem1 == elem2):

                cont += 1

            if(cont > 1):

                array4.remove(elem1)

    return array4


array1 = [1,2,3,4,5,6,7,8,9,9,9,9]

array2 = [5,10,3,66,1,4,9]

array3=crear_array(array1,array2)

print(eliminar_repetido(array3))
