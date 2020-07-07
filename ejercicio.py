"""
***************************************************************************
* Nombre: gestion_flota.py                                                *
* OBJ: Programa que gestiona los datos de una flota de turismos.          *
***************************************************************************
"""

COSTES = [[22.00,8.30,10.5],[150,100,50]] #Precio/hora -- fianza tipo coche

MANT = [75.42, 17.71, 22.42, 23.63, 19.83]

COCHES = [1, 2, 3, 3, 2] # 1(furgo), 2(4plazas), 3(5plazas)

HORAS = [10.00, 72.00, 30.00, 32.50, 28.50]

TIPOS = ['furgo','4p','5p']

FLOTA = ['04410FJB', '2222HIJ', 'MU-1388', '8888XYZ', '9999XYK']

INGR_COCHE = [220.00, 597.60, 315.00, 341.25, 236.55]

def ingr_indvdual(COSTES, COCHES, HORAS, MANT):

    """ tupla, tupla, tupla, tupla --> tupla
    OBJ: Dterminar el ingreso de cada coche.
    PRRE: Nada. """


def ingr_total(HORAS, COSTES,TIPOS):

    """ tupla, tupla, tupla --> float
    OBJ: Devuelve la suma de todos los ingresos.
    PRE: Nada. """

    total = 0

    for i in range(len(HORA)):

        total += HORAS[i]*COSTES[0][TIPO[i]-1]

    return round(total,2)

def mayor_ingreso(INGR_COCHE):

    """ tupla --> int
    OBJ: Devuelve la posicion en la que esta vehiculo >> ingreso.
    PRE: Nada. """

    pos_mayor = 0

    for i in range(1, len(FLOTA)):

        if (INGR_COCHE[i] > INGR_COCHE[pos_mayor]):

            pos_mayor = i

    return pos_mayor

def tipo_coche(TIPOS,COCHES):

    """ tupla, tupla --> tupla
    OBJ: Devuelve el tipo de coche.
    PRE: Nada. """

    coche = COCHES

    for i in range(len(COCHES)):

        coche[i] = TIPOS[COCHES[i]-1]

    return coche

from libInterfaz import enteroPedido

"""n_coches = enteroPedido(0,50,"Cuantos coches desea introducir: ")

for cont in range(n_coches):

    FLOTA.insert(cont,input("Matricula del coche(7 digitos): "))
    MANT.insert(cont,enteroPedido(0,100,"Coste dde mantenimiento: "))
    COCHES.insert(cont,enteroPedido(1,3,"Categoria: "))
    HORAS.insert(cont,enteroPedido(0,700,"Hora que ha sido  utilizado: "))"""

def imprimir_tabla(FLOTA,MANT,COCHES,HORAS,INGR_COCHE):

    """ tupla, tupla,tupla --> Nada
    OBJ: Imprimir por pantalla  una tabla con los resultados obtenidos.
    PRE: Nada. """

    coche = tipo_coche(TIPOS,COCHES)

    ingresos = ingr_indvdual(COSTES, COCHES, HORAS, MANT)

    pos = mayor_ingreso(INGR_COCHE)

    print("Matricula    |      Tipo     |     alq/h     |     h     |     mant     |     fianza     |     ingresos     |     estrella")

    print()

    for i in range(len(FLOTA)):

        print(FLOTA[i],end='          ')

        print(coche[i],end='             ')

        if(coche[i] == 'furgo'):

            print(COSTES[0][0],end='          ')

        elif(coche[i] == '4p'):

            print("    ",COSTES[0][1],end='          ')

        else:

            print("   ",COSTES[0][2],end='          ')

        print(HORAS[i],end='         ')

        print(MANT[i],end='        ')

        if(coche[i] == 'furgo'):

            print("  ",COSTES[1][0],end='             ')

        elif(coche[i] == '4p'):

            print("  ",COSTES[1][1],end='             ')

        else:

            print("  ",COSTES[1][2],end='              ')

        print(INGR_COCHE[i],end='                  ')

        if(i == pos):

            print("*")

        else:

            print("   ")

imprimir_tabla(FLOTA,MANT,COCHES,HORAS,INGR_COCHE)



        





        

        

    
    

        















































