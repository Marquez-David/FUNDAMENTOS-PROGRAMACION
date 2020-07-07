"""

    Nombre: Multiplo de Tres.
    OBJ: Determina si un numero es multiplo de tres.
    PRE: El numero introducido debe ser un entero.

"""

def multiplo_de_tres(numero):

    if(numero % 3 == 0):

        print("Es primo")

    else:

        print("No es primo")

multiplo_de_tres(int(input("Introduce un numero: ")))
