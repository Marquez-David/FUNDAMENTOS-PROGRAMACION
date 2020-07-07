def iguales_o_cinco(num1,num2):

    """
    int , int --> Nada
    OBJ: Determina si dos numeros son = o su +/- = 5.
    PRE: Los numeros deben ser enteros.
    """

    if(num1 == num2):

        print("Numeros iguales. ")

    elif(num1 + num2 == 5):

        print("La suma = 5")

    elif(num1 - num2):

        print("La resta = 5")

try:
    
    iguales_o_cinco(int(input("Num 1: ")), int(input("Num 2: ")))

except ValueError :

    print("Los numeros deben ser enteros. ")
    
