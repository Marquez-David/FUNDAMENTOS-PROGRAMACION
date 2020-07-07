"""
****************************************************************************
* Nombre: mostrar_serie_fracciones.py                                      *
* OBJ: Mostar una serie de fraccioes porpantalla.                          *
****************************************************************************
"""

def mostrar_serie(num):

    """ int --> Nada
    OBJ: Mostrar una serie de fracciones por pantalla.
    PRE: El termino num debe ser entero. """

    numerador = 1

    denominador = 2

    numerador_ant = 0
    
    denominador_ant = 0

    for i in range(num):

        numerador_ant = numerador

        denominador_ant = denominador

        print(numerador_ant,"/",denominador_ant,end='        ')

        numerador = numerador + denominador_ant

        denominador = numerador_ant + numerador_ant*denominador_ant

mostrar_serie(4)

        
    
