"""
*******************************************************************************
* Nombre: fibo_recur.py
* OBJ: Sucesion de fibonacci recursivo.
*******************************************************************************
"""

#Aumentar el tamaño de la pila.
"""
import sys
sys.setrecursionlimit(90000)""" 

def fibo(num): # num es eltermino n de la sucesion.

    """ int -> int
    OBJ: Sucesion fibonacci hasta eltermino 'num'.
    PRE: 0<=num. """
    
    if(num == 0): a = 0

    if(num == 1): a = 1

    else:

        a = fibo(num-1) + fibo(num-2)

    return a

print(fibo(4))
