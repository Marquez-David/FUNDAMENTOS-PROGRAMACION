"""
********************************************************************************
* Nombre: tam_seg.py
* OBJ: Tamanio del un segmento.
********************************************************************************
"""

from collections import namedtuple

tPunto = namedtuple('Punto',['x','y'])

tSegmento = namedtuple('Segmento','pIni, pFin')

def tamanio(p1,p2): #Le pasamos los puntos extremos del segmento.

    """ tPunto, tPunto -> float
    OBJ: Distancia del segmento.
    PRE: tPunto deben servalores positivos. """

    from math import sqrt

    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def p_random():

    """ Nada -> tPunto
    OBJ: crear un punto aleatorio 0<=x, 0<=y. """

    from random import random

    x = random()

    y = random()

    return tPunto(x,y)

print(p_random())














    
'''
#Probador

ini = tPunto(1.0,1.0)

fin = tPunto(2.0,2.0)

print('El tamaño del segmento es: ', tamanio(ini,fin))

seg = tSegmento(ini,fin)

print('El segmento mide: ', tamanio(seg.pIni,seg.pFin))'''

    
