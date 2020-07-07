"""
*******************************************************************************
* Nombre: limpiar_frase.py
* OBJ: Limpiar una frase de blancos indeseados.
*******************************************************************************
"""

def limpieza(frase):

    """ str -> str
    OBJ: Limpiar un str.
    PRE: Nada. """

    frase = frase.capitalize().strip().title()
    
    letra_anterior =''

    resultado = ''

    for letra in frase:

        if(letra == letra_anterior):

            letra = ''

        else: 

            letra_anterior = letra

        resultado += letra

    return resultado

def pedir_dato(dato):

    """ str -> str
    OBJ: Pide un Nombre/Apellido1/Apellido2
    PRE: Nada. """

    return limpieza(dato)

#Probador
#print(limpieza(' daVid     MarqueZ minGuez  '))
print(pedir_dato(str(input('Introduce Nombre o Appelido1 o Apellido2: '))))
