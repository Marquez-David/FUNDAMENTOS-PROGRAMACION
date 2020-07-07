"""
*******************************************************************************
* Nombre: potencia_recursivo.py
* OBJ: Calcula la potencia de un numero.
*******************************************************************************
"""

def potencia(num,grado):

    """ int, int -> int
    OBJ: Potencia grado de num.
    PRE: grado >= 0. """

    a = 1

    if(grado == 1 or grado == -1):

        a = num

    elif(es_negativo(grado)):

        a = 1 / (num * potencia(num,grado+1))

    else:

        a = num * potencia(num,grado-1)

    return a

def es_negativo(num):

    """ int -> bool
    OBJ: Si un numero es negtivo.
    PRE: Nada. """

    negativo = True

    if(num>0):

        negativo = False

    return negativo

#Prueba
print(potencia(2,-2))
print(potencia(2,2))

        
