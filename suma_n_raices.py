"""
*****************************************************************************
* Nombre: suma_n_raices.py                                                  *
* OBJ: Calcula la  suma de las n raices.                                    *
*****************************************************************************
"""

def suma_raices(num):

    """ int --> float
    OBJ: Calcula la suma de numraices.
    PRE: Los numerosintroducidos deben ser enteros. """

    suma = 0

    for i in range(1,num+1):

        suma += (i)**(1/2)

    print(suma)

suma_raices(3)
