"""
******************************************************************************
* Nombre: menu_matematico.py                                                 *
* OBJ: Muestra por pantalla un menu, el usurio elige la opcion.              *
******************************************************************************
"""

def elegir_opcion():

    """ Nada --> Nada
    OBJ: Determina la opcion que va a elegir el usuario.
    PRE: Nada. """

    print("Opcion 0: El programa termina. ")
    print("Opcion 1: Verificar un numero par de cuatros cifras. ")
    print("Opcion 2: Mostrar un numero aleatorrio por pantalla. ")
    print("Opcion 3: Factorial de un numero. ")
    print()

    opcion = int(input("Que opcion deseas: "))

    if(opcion == 0):

        print("Fin del programa. ")

    elif(opcion == 1):

        mostrar_par_4_cifras()

    elif(opcion == 2):

        mostar_numero_aleatorio()

    elif(opcion == 3):

        factorial_num()

    else:

        print("ERROR: Eleccion incorrecta el numero no esta entre las opciones. ")



def factorial_num():

    """ Nada --> Nada
    OBJ: Calcula el factorial de un numero.
    PRE: El numero debe ser entero. """

    factorial = 1

    num = int(input("Introduce un numero: "))

    for i in range(1,num+1):

        factorial *= i

    print("El factorial de",num,"es: ",factorial)



def es_par(num): #Funcion auxiliar 

    """ int --> bool
    OBJ: Determina si un numero es par.
    PRE: El numero introducido debe ser un entero. """

    par = False

    if(num %2 == 0):

        par = True

    return par

def tiene_4_cifras(num): #Funcion auxiliar

    """ int --> bool
    OBJ: Determina si un numero tiene cuatro cifras:
    PRE: El numero introducido debe ser entero. """

    cuatro_cifras = False

    if((num // 1000) -10 < 0 and (num // 1000) -10 > -10):

        cuatro_cifras = True

    return cuatro_cifras

def mostrar_par_4_cifras():

    """ Nada -->  Nada
    OBJ: Imprime por pantalla si un numero es impar y si tiene 4 cifras
    PRE: Nada. """

    num = int(input("Introduc un numero: "))

    if(es_par(num)):

        print("El numero es par. ")

    elif(es_par(num) == False):

        print("El numero es impar. ")

    if(tiene_4_cifras(num)):

        print("Tiene 4 cifras. ")

    else:

        print("No tiene 4 cifras. ")

def mostar_numero_aleatorio():

    """ Nada --> Nada
    OBJ: Muestra por pantalla un numero aleatorio.
    PRE: Nada. """

    num = int(input("Introduce un numero: "))

    if(es_par(num) == 0 or tiene_4_cifras(num) == 0):

        print("ERROR: el numero o es impar o no tiene 4 cifras. ")

    else:

        num = num ** 2

        num = num // 10000

        print(num)
 

elegir_opcion()



