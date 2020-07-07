"""
**********************************************************************
* Nombre: calculadora.py                                             *
* OBJ: Realiza una serie de operaciones,e usuario elige cual.        *
**********************************************************************
"""

def calculadora(num1,num2):

    """ float, float --> Nada
    OBJ: Realiza la oeracion que el usuario decida.
    PRE: La opcion elegida debe estar entre 0 y 4. """

    print("Opcion 0: No se realiza ninguna operacion y finaliza el programa. ")
    print("Opcion 1: Realiza la suma entre dos numeros. ")
    print("Opcion 2: Realiza la resta entre dos numeros. ")
    print("Opcion 3: Realiza la multiplicaccion entre dos numeros. ")
    print("Opcion 4: Realizala division entre dos numeros. ")

    opcion = int(input("Que opcion deseas: "))

    while (opcion != 0):

        if(opcion == 1):

            resultado = num1 + num2

            print("La suma es: ", resultado)

        elif(opcion == 2):

            resultado = num1 - num2

            print("La resta es: ", resultado)

        elif(opcion == 3):

            resultado = num1*num2

            print("La multiplicacion es: ", resultado)

        elif(opcion == 4):

            resultado = num1 / num2

            print("La division es: ", resultado)

        else:

            print("Introduce una opcion correcta. ")

        opcion = int(input("Que opcion deseas: "))

calculadora(3,6)

        

        

