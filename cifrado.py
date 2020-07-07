"""
*******************************************************************************
* Nombre: cifrado.py
* OBJ: Cifrar una str.
********************************************************************************
"""

ALFABETO = ('A','B','C','D','E','F','G','H','I','J',
            'K','L','M','N','O','P','Q','R','S','T',
            'U','V','W','X','Y','Z')

def cifrado(n,frase,ALFABETO):

    """ int, str -> str
    OBJ: Cifrar un str. """

    palabra = frase.upper()

    lista_palabra = []

    nF = len(frase) #Numero letras de la frase

    nA = len(ALFABETO) #Numero letras alfabeto

    for i in range(nF): #Recorre la frase

        for j in range(nA): #Recorre el alfabeto

            if(palabra[i] == ALFABETO[j]):

                lista_palabra.append(ALFABETO[j+n])

    return ''.join(lista_palabra) # Convertir lista en str

print(cifrado(2,'hola',ALFABETO))

    
