"""
****************************************************************************
* Nombre: mostrar_onda.py                                                  *
* OBJ: Muestra una onda de numeros enteros siguiendo una secuencia.        *
****************************************************************************
"""

def mostrar_onda(num_ini,num_central,num_fin,rep):

    """ int, int, int, int --> Nada
    OBJ: Muestra una onda de enteros siguiendo una secuencia.
    PRE: Los numeros  introducidos deben ser enteros. """

    print(num_ini,end='-')

    for l in range(rep):#Numero de veces que se repite la onda

        for i in range(num_ini+1,num_central+1): #Del inicio al centro

            print(i,end='-')

        for j in range(num_central-1,num_fin,-1):#Del cntro al fin

            print(j,end='-')

        for k in range(num_fin,num_ini+1):#Del fin hasta ini

            print(k,end='-')



        

mostrar_onda(5,8,-1,2)
