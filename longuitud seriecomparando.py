def serie_numeros_enteros(numero):
    """int-->int
    OBJ: determina la longuitud de la serie de numeros proporcionados por el usuario.
    PRE: los numeros deben ser enteros. """
    longuitud_serie = 0
    CENTINELA = -9999
    num_anterior = 0
    longuitud_serie_anterior = 0
    while ( numero != CENTINELA):
        numero= numero_anterior
        numero = int(input("Introduce un numero de la serie(-9999 para terminar): "))
        if (num_anterior + 1 == numero):
            longuitud_serie = longuitud_serie + 1
        if (longuitud_serie > longuitud_serie_anterior):
            print("La longuitud de la serie es: " ,  longuitud_serie)
try:
    serie_numeros_enteros(int(input("Introduce un numero de la serie(-9999 para terminar): ")))
except:
    print("Los numeros deben ser enteros")
