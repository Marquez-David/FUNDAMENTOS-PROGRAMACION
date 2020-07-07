"""
***************************************************************************
* Nombre: menu_opciones.py                                                *
* OBJ: Segun la opcion elegida, realiza diferentes acciones.              *
***************************************************************************
"""

def menu_opciones():

    """ int --> Nada
    OBJ: Segun la opcion elegida realiza diferentes acciones.
    PRE: La opcion elegida debe ser un numero entero. """

    print(" Opcion 0: El programa termina. ", "\n",
          "Opcion 1: Verifica si un numero es par ytiene cuattro cifras. ","\n",
          "Opcion 2: Generar numeros pseudo_aleatorios. ", "\n",
          "Opcion 3: Numero factorial. ")

    opcion = int(input("Que opcion eliges: "))

    if(opcion < 0 or opcion > 4):

        print("Error: Esa opcion de existe. ")


    elif(opcion == 1): #Opcion 1

        num_op1 = int(input("Numero: "))

        if (num_op1%2== 0):

            print("Numero es par. ")

        elif(num_op1%2 != 0):

            print("El numero es impar. ")

        if(num_op1/1000 >= 1):

            print("El numero tiene 4 cifras. ")

        else:

            print("El numero tiene menos de 4 cifras. ")

    elif(opcion == 2): #Opcion 2

        num_op2 = int(input("Numero: "))

        num_cuadrado = 0

        centenas = 0

        unidades_mil = 0

        decenas_mil = 0

        centenas_mil = 0

        if(num_op2/1000 < 1 or num_op2%2 != 0 or num_op2/1000 > 10):

            print("Error: El numero es impar o tiene mas/menos de 4 cifras. ")

        else:

            num_cuadrado = num_op2**2

            centenas_mil = num_cuadrado // 10000000

            decenas_mil = (num_cuadrado // 1000000) - centenas_mil*10

            unidades_mil = (num_cuadrado // 100000) - (decenas_mil*10 + centenas_mil*100)

            centenas = (num_cuadrado // 10000) - (decenas_mil*100 + centenas_mil*1000+unidades_mil*10)

            print("Numero Introducido: ",num_op2 ,"Primer numero: ",centenas_mil,"Segundo numero: ",decenas_mil,"Tercer numero: ",unidades_mil,
                  "Cuarto numero: ",centenas)

    elif(opcion == 3): #Opcion 3

        num_op3 = int(input("Numero: "))

        resultado = num_op3

        for numero in range(num_op3-1):

            resultado *= numero+1

        print("Numero: ", num_op3, "Factorial: ", resultado)

menu_opciones()
