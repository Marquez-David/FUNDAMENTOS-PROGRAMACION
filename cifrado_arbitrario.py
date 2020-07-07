"""
*******************************************************************************
* Nombre: cifrado_arbitrario.py
* OBJ: Cifra un str.
*******************************************************************************
"""

ALFABETO = ('A','B','C','D','E','F','G','H','I','J',
            'K','L','M','N','O','P','Q','R','S','T',
            'U','V','W','X','Y','Z')


CODIF =('Q','C','D','J','E','L','O','P','M',
        'R','K','S','N','A','T','U','X','G',
        'Z','B','F','H','I','Y','V')

def codificacion(frase,ALFABETO,CODIF):

    """ str, tupla,tupla -> str
    OBJ: Codificar un str. """

    palabra = frase.upper()

    lista_palabra = []

    nF = len(frase) #Numero letras de la frase

    nA = len(ALFABETO) #Numero letras alfabeto

    for i in range(nF): #Recorre la frase

        for j in range(nA): #Recorre el alfabeto

            if(palabra[i] == ALFABETO[j]):

                lista_palabra.append(CODIF[j])

    return ''.join(lista_palabra) # Convertir lista en str

#Probador
print(codificacion('hola',ALFABETO,CODIF))

    
