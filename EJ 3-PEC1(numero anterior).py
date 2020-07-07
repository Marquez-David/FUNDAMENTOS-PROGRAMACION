def secuencia_de_numeros(limite):
    """int-->int
    OBJ: determinar una secuencia creciente de numeros cuya longuitud es dicha por el usuario e imprimira por pantalla los numeros decartados. """
    cantidad_total = 0
    descartes_total = 0
    num_anterior = 0
    import random
    while ( cantidad_total < limite ):
        numero = random.randint(1,limite)
        cantidad_total = cantidad_total + 1
        if ( numero < num_anterior ):
            descartes_total = descartes_total + 1
        print(numero)
        num_anterior = numero
    print("El numero total de numeros ha sido: " ,  cantidad_total)
    print("El numero de descartes ha sido: "  , descartes_total)
try:
    secuencia_de_numeros(int(input("Introduce la longuitud de la secuencia: ")))
except:
    print("La longuitud de la secuencia debe ser un numero entero")
