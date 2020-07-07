"""
************************************************************************
* Nombre: entre_limites.py                                             *
* OBJ: Muestra la distancia minima entre numero y limites.             *
************************************************************************
"""

def entre_limites(num,lim_sup,lim_inf):

    """ int, int, int --> Nada
    OBJ: Muestra la distancia minima entre num y los limites
    PRE: Los numeros introducidos deben ser enteros. """

    if (lim_inf<num and num<lim_sup):

        if(abs(lim_inf - num) < abs(lim_sup - num)):

            for numero in range(lim_inf+1,num+1):

                print(numero)

        else:

            for numero in range(num+1,lim_sup+1):

                print(numero)
                
    else:

        print("El numero no se encuentra entre los limites. ")

entre_limites(35,40,20)
