"""

    Nombre: De  nnumero a espaniol.
    OBJ: Muestra un numero en espaniol.
    PRE: Los numeros deben ser > 0 y < 99.

"""

def muestra_numeros(numero):

    """ int --> Nada
    OBJ: Muestra un numero en español.
    PRE: 0 < numero < 99.
    """

    if ( 16 <= numero <= 19):

        numero = numero % 10

        print("Diez y ")

    if (20 <= numero <= 29):

        numero = numero % 10

        print("Veinte y ")

    if(30 <= numero <= 39):

        numero = numero % 10

        print("Treinta y ")

    if ( 40 <= numero <= 49):

        numero = numero % 10

        print("Cuarenta: y ")

    if ( 50 <= numero <= 59):

        numero = numero % 10

        print("Cincuenta y " )

    if ( 60 <= numero <= 69):

        numero = numero % 10

        print("Sesenta y ")

    if ( 70 <= numero <= 79):

        numero = numero % 10

        print("Setenta y ")

    if ( 80 <= numero <= 89):

        numero = numero % 10

        print("Ochenta y " )

    if ( 90 <= numero <= 99):

        numero = numero % 10

        print("Noventa y  " )

    if ( numero == 0): print(" ")

    elif ( numero == 1): print("Uno ")

    elif( numero == 2): print("Dos ")

    elif( numero == 3): print("Tres ")

    elif( numero == 4):  print("Cuatro ")

    elif( numero == 5): print("Cinco ")

    elif( numero == 6): print("Seis ")

    elif( numero == 7): print("Siete ")

    elif( numero == 8): print("Ocho ")

    elif( numero == 9): print("Nueve ")

    elif( numero == 10): print("Diez ")

    elif( numero == 11): print("Once ")

    elif( numero == 12): print("Doce ")

    elif( numero == 13): print("Trece ")

    elif( numero == 14): print("Catorce ")

    elif( numero == 15): print("Quince ")

try:

    muestra_numeros(int(input("Numero: ")))

except ValueError:

    print("Los valores introducidos deben ser numeros enteros. ")

    
    
