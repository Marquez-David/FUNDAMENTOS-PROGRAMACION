"""
*******************************************************************************
* Nombre: combinatoria.py
* OBJ: Menu que oofrece aplicaciones combinatorias.
********************************************************************************
"""

from entre_limites import limites

def menu():

    """ Nada -> Nada
    OBJ: Menu con opciones para el usuario.
    PRE:  Nada. """

    mensaje = 'Introduce otro numero: '

    print('\t\t\t COMBINAORIA')
    print('\t\t\t ============')

    print('1.-Variaciones')
    print('2.-Combinaciones')
    print('3.-Permutaciones')
    print('4.-Salir')

    opcion = limites(1,4,mensaje)

    while (opcion != 4):

        if(opcion == 1):

            print('Variaciones: ')

            print(variaciones(int(input('Num1: ')), int(input('Num2: '))))

        elif(opcion == 2):

            print('Combinaciones: ')

            print(combinaciones(int(input('Num1: ')), int(input('Num2: '))))

        elif(opcion == 3):

            print('Permutaciones: ')

            print(permutaciones(int(input('Num1: '))))


        #Simulamos bucle 1-n ya que en python no existe
        opcion = limites(1,4,mensaje)

def variaciones(m,n):

    """ int, int -> float
    OBJ: m!/(m-n)!
    PRE: m y n > 0. """

    return factorial(m)/factorial(m-n)

def permutaciones(m):

    """ int -> int
    OBJ: n!
    PRE: m >0. """

    return factorial(m)

def combinaciones(m,n):

    """ int, int -> float
    OBJ: V(m,n)/P(n)
    PRE: m, n >0. """

    return variaciones(m,n)/permutaciones(n)

def factorial(m): #Operacion auxiliar

    """ int -> int
    OBJ: Calcular el factorial m!
    PRE: m > 0. """

    sol = 1 #Para poder realizar el 'multiplicatorio'

    while m>0:

        sol *= m

        m -= 1

    return sol
    
#Probador
menu() 
