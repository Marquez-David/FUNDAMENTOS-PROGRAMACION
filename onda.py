"""
****************************************************************************
* Nombre: onda.py                                                          *
* OBJ: Mostrar onda.                                                       *
****************************************************************************
"""

def mostrar_onda(num_ini,num_fin,num_cntr,num_rep):

    """ int, int, int, int --> Nada
    OBJ: Mostrar una onda de numeros enteros.
    PRE: Los datos introducidos deben ser enteros. """

    #5.6.7.8.7.6.5.4.3.2.1.0.-1.0.1.2.3.4.5.6.7.8.7.6.5.4.3.2.1.0.-1.0.1.2.3.4.5

    num = num_ini # Variable que repetrsenta el numero.

    print(num,end=' ')

    for rep_serie in range(num_rep): # Veces que se repite la serie entera

        for rep in range(num_ini+1): # Desde -1 hasta 5

            if(num<num_ini):

                num += 1

                print(num, end=' ')
            
        for rep in range(num_cntr-num_ini): # Desde 5 hasta 8

            if(num <= num_cntr):

                num += 1

                print(num,end=' ')

        for rep in range(num_cntr - num_fin): # Desde 8 hast -1

            if(num <= num_cntr and num > num_fin ):

                num -= 1

                print(num,end=' ')

    for rep in range(num_ini+1): # Desde -1 hasta 5

        if(num<num_ini):

            num += 1

            print(num, end=' ')

mostrar_onda(5,-1,8,2)
