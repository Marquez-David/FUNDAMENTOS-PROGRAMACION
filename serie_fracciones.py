"""
****************************************************************************
* Nombre: serie_fracciones.py                                              *
* OBJ: Calcula la serie entre 1 y n.                                       *
****************************************************************************
"""

def serie_fracciones(num):

    """ int --> Nada
    OBJ: Calcula la serie entre 1 y n.
    PRE: num debe ser un numero entero. """

    numer_ini = 1

    denom_ini = 2

    numer_fin = 1

    denom_fin = 2

    for num_iteraciones in range(num):

        print(numer_fin, "/", denom_fin)

        numer_fin = numer_ini + denom_ini

        denom_fin = numer_ini + (numer_ini*denom_ini)

        numer_ini = numer_fin

        denom_ini = denom_fin

serie_fracciones(4)

        
