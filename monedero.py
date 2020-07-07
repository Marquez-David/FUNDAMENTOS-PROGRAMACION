"""
***************************************************************************************
* Nombre: monedero.py                                                                 *
* OBJ: Cuantos billetes tipo,suma de billtes tipo, suma total,si hay monedas tipo.    *
***************************************************************************************
"""

MONED_EU = [500.0,200.0,100.0,50.0,20.0,10.0,5.0,2.0,1.0,0.5,0.2,0.1,0.05,0.02,0.01]

def billetes_cada_tipo(MONED_EU):

    """ int,list --> list
    OBJ: Determina cuantos billetes hay de cada tipo.
    PRE: El numero de billetes debe ser un entero. """

    monedero_actual = []#Creamos una lista con el numero de billetes que hay de cada tipo.

    for i in range(len(MONED_EU)):

        print("Introduce el numero de billetes que hay de",MONED_EU[i],end='')

        cuant = int(input(": "))

        monedero_actual.append(cuant) #La posicion del numero de billetes se corresponde con el tipo.

    return monedero_actual

def suma_cada_tipo(monedero_actual,MONED_EU):

    """ list, list --> list
    OBJ: Cuanto dinero hay de cada tio de billetes.
    PRE: Nada. """

    lista_suma = []#Creamos una lista, cada posicion tendra la cantidad dinero que hay de cada de billete.

    for j in range(len(MONED_EU)):

        suma = monedero_actual[j] + MONED_EU[j]

        lista_suma.append(suma)#La posicion de la cantidad de dinero corresponde con el tipo.

    return lista_suma

def suma_total(lista_suma):

    """ list --> float
    OBJ: Cantidad total que hay de dinero.
    PRE: Nada. """

    total = 0.0

    for dinero in lista_suma:

        total += dinero

    return total

def mostrar_datos(MONED_EU,monedero_actual,lista_suma,total):

    """ list, list, float --> Nada
    OBJ: Mostrar por pantalla en una tabla los datos.
    PRE: Nada. """

    print()

    print("TIPO DE BILLETES", end='     |     ')
    print("NUMERO DE BILLETES",end='    |     ')
    print("DINERO DE CADA TIPO  | ")
    print("-----------------------------------------------------------------------------")

    for l in range(len(MONED_EU)):

        print(MONED_EU[l],end='                            ')
        print(monedero_actual[l],end='                            ')
        print(lista_suma[l])
        print("-----------------------------------------------------------------------------")

    print()

    print("TOTAL = ", total)

    
        


monedero_actual = billetes_cada_tipo(MONED_EU)

lista_suma = suma_cada_tipo(monedero_actual,MONED_EU)

total = suma_total(lista_suma)

mostrar_datos(MONED_EU,monedero_actual,lista_suma,total)
