"""
***************************************************************************************
* Nombre: descomp_numerica.py                                                          *
* OBJ: Descompone un numero en decenas,centenas,unidades...                           *
***************************************************************************************
"""

def descomp_numerica(num):

    """ int --> Nada
    OBJ: Descompone un numero en decenas, centenas, unidades...
    PRE: num debe ser un entero. """

    n = numero_cifras

    residuo = 0

    while (n>=1):

        residuo = num % 10**(n-1)

        num = num // 10**(n-1)

        n -= 1

        print(num,end=' ')

        num = residuo

def cuantas_cifras(num):

    """ int --> int
    OBJ: Determina cuantas cifras tiene un numero.
    PRE: Nada. """

    divisor = 10

    cont = 1

    while ((num // divisor) != 0 ):

        cont+= 1

        divisor *= 10

    return cont
        
numero_cifras = cuantas_cifras(123456789)
descomp_numerica(123456789)


    

    
    
