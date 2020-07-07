#Ejercicio 9-C4
def vocales_en_palabra(palabra):
    """ str --> boolean
    OBJ: determina si una palabra contiene las cinco vocales. """
    listaPalabra = []
    listaPalabra = list(palabra)
    contadorA = 0
    contadorE = 0
    contadorI = 0
    contadorO = 0
    contadorU = 0
    for elem in listaPalabra:
        if elem == "a":
            contadorA = contadorA + 1
        elif elem == "e":
            contadorE = contadorE + 1
        elif elem == "i":
            contadorI = contadorI + 1
        elif elem == "o":
            contadorO = contadorO + 1
        elif elem == "u":
            contadorU = contadorU + 1
    if contadorA >=1 and contadorE >=1 and contadorI >=1 and contadorO >=1 and contadorU >=1:
        return True
    else:
        return False













#Programa Probador
palabra = "hola"
#palabra = "murcielago"
vocales_en_palabra(palabra)