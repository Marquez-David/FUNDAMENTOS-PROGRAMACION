"""
*************************************************************************
* Nombre: suma_matr_colum.py                                            *
* OBJ: Suma matrices y columnas de matriz resultante.                   *
*************************************************************************
"""

def suma_matrices(m1,m2):

    """ lista,lista --> lista
    OBJ: Suma dos matrices.
    PRE: Las matrices deben tener elmismo tamanio. """

    m3 = []

    for i,j in zip(m1,m2):

        lista_suma = []

        for k,l in zip(i,j):

            lista_suma.append(k+l)

        m3.append(lista_suma)

    return m3

def suma_columna(m_final):

    """ lista --> lista
    OBJ: Suma las columnas de una matriz.
    PRE: Nada. """

    m4 = []

    suma = 0

    for i in range(len(m_final)):

        suma = 0 #Reinicamos la suma en cada columna

        for j in range(len(m_final)):

            suma += m_final[j][i]

        m4.append(suma)

    return m4
    
m1 = [[2,0,1],[3,0,0],[5,1,1]]

m2 = [[1,0,1],[1,2,1],[1,1,0]]

m_final = suma_matrices(m1,m2)

suma_columna(m_final)
