"""
****************************************************************************
* Nombre: distancia_min.py                                                 *
* OBJ: Si un numero esta entre limites y calcular la distancia minima.     *
****************************************************************************
"""

def esta_entre(num,lim_sup,lim_inf):

    """ int,int,int --> bool
    OBJ: Determina si unnnnumero esta entre limites.
    PRE: lim_sup > lim_inf. """

    entre_lim = False

    if (num > lim_inf and num < lim_sup):

        entre_lim = True

    return entre_lim

def mostrar_min(esta,num,lim_sup,lim_inf):

    """ bool, int,int,int --> Nada
    OBJ: Muestra por pantalla la serie mas pequeña limites.
    PRE: Nada ."""

    dist_min_sup = lim_sup - num

    dist_min_inf = abs(lim_inf - num)

    if(esta == False):

        print("El numero no esta entre los limites. ")

    elif( dist_min_sup < dist_min_inf ):

            for i in range(num,lim_sup+1):

                print(i,end=' ')

    else:

        for j in range(lim_inf,num+1):

            print(j,end=' ')
                
esta = esta_entre(25,40,20)
mostrar_min(esta,25,40,20)
