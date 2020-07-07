"""

    Nombre: Suma de numeros.
    OBJ: Suma numeros si se cumple unas condiciones.

"""

def suma_numeros(n1,n2,n3):

    """ float, float, float --> float
    OBJ: suma tres numeros si se cumplen unas condiciones.
    """

    if ( n1 == n2 or n1 == n3 or n2 == n3):

        resultado = 0

    else :

        resultado = n1 + n2 + n3

    print("Resultado: ", resultado)

    return resultado

try:

    suma_numeros(float(input("Numero1: ")), float(input("Numero2: ")), float(input("Numero3: ")))

except ValueError:

    print("Debe introducir valores numericos. ")
