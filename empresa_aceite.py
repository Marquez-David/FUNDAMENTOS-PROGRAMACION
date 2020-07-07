"""
********************************************************************************
* Nombre: empresa_aceite.py
* OBJ: Gestionar una empresa exportadora de aceite.
********************************************************************************
"""

from collections import namedtuple

tAceite = namedtuple('Aceite','tipo, origen, destino, fecha_envasado,\
                        num_pedido, cantidad, precio_litro, precio_total')

tFecha = namedtuple('Fecha', 'dia, mes, anno')

tipo = ('virgen extra', 'oliva', 'orugo de oliva')

precio = (3.67,3.46,3.15)

#Probador

fecha1 = tFecha(2,4,2006)
aceite1 = tAceite(tipo[0],'Cadiz','Madrid',fecha1,'1234E',20,precio[0],50)
#print(aceite1)

fecha2 = tFecha(4,9,2016)
aceite2 = tAceite(tipo[1],'Barcelona','Zaragoza',fecha2,'2345F',50,precio[1],35)
#print(aceite2)

fecha3 = tFecha(30,6,2009)
aceite3 = tAceite(tipo[2],'Valencia','Galicia',fecha3,'4567G',13,precio[2],24)
#print(aceite3)

fecha4 = tFecha(31,2,2019)
aceite4 = tAceite(tipo[1],'Madrid','Zaragoza',fecha4,'5678HF',10,precio[1],12)
#print(aceite2)

aceites = [aceite1, aceite2, aceite3, aceite4]

def calculo_precio(aceites,identif):

    """ tupla, str -> float
    OBJ: Precio de un pedido, -1 si el  producto no existe.
    PRE: El num_pedido debe existir."""

    precio_tot = -1

    for aceite in aceites:

        if(aceite.num_pedido == identif):

            precio_tot = aceite.cantidad * aceite.precio_litro

    return precio_tot

            
#Probador
#print(calculo_precio(aceites,'1234E'))
#print(calculo_precio(aceites,'2345F'))
#print(calculo_precio(aceites,'4567G'))

def mostrar_productos(aceites,n_tipo):

    """ tupla, int -> Nada
    OBJ: Muestra por pantalla listado de productos.
    PRE: 0<=tipo<=2. """

    from centrar_rotulo import centrar_rotulo

    for aceite in aceites:

        if(aceite.tipo == aceites[n_tipo].tipo):

            centrar_rotulo('Aceites del tipo ' + tipo[n_tipo],'=')
            print('Datos del producto: ')

            print('Tipo: ', tipo[n_tipo])
            print('Origen: ',aceite.origen)
            print('Destino: ', aceite.destino)
            print('Fecha envasado: ', aceite.fecha_envasado.dia,'/',aceite.fecha_envasado.mes,'/',
                                aceite.fecha_envasado.anno,sep='')
            print('Num pedido: ', aceite.num_pedido)
            print('Cantidad: ', aceite.cantidad)
            print('Precio/Litro: ', aceite.precio_litro)
            print('Precio: ', calculo_precio(aceites,aceites[n_tipo].num_pedido))

#Probador
#mostrar_productos(aceites,1)

def lugares_venta(aceites):

    """ tupla -> lista
    OBJ: Crear una tupla con los ligares vendidos.
    PRE: Nada. """

    lugares = []

    for aceite in aceites:

        if(aceite.destino not in lugares):

            lugares.append(aceite.destino)

    return lugares

#Probador
#print(lugares_venta(aceites))

def litros_vendidos(aceites):

    """ tupla -> lista
    OBJ: Imprime los litros vendidos a cada destino.
    PRE: Nada. """

    lugares = lugares_venta(aceites)

    ventas = []

    total_vendido = 0

    for ciudad in lugares:

        total_vendido = 0

        for aceite in aceites:

            if(ciudad == aceite.destino):

                total_vendido += aceite.cantidad

        ventas.append(total_vendido)

    return ventas 

#Probador       
#print(litros_vendidos(aceites))

def lugar_mayor_venta(aceites):

    """ tupla -> str
    OBJ: Ciudad con mayor numero de ventas.
    PRE: Nada. """

    ventas = litros_vendidos(aceites)
    ciudades = lugares_venta(aceites)
    litro_mayor = 0
    pos = -1 # -1 porque va a entrar en 1 +1 si o si.

    for litros in ventas:

        if(litro_mayor<litros):

            litro_mayor = litros
            pos +=1

    return ciudades[pos]

#Probador
#print(lugar_mayor_venta(aceites))

def total_exportadoR(pos,ventas):

    """ int, lista -> float
    OBJ:Litros vendidos en total rcursivo.
    PRE: 0<=pos<=len(ventas)-1. """

    total = 0

    if(pos <= len(ventas)-1):

        total = ventas[pos] + total_exportadoR(pos+1,ventas)

    return total

#Probador
#ventas = litros_vendidos(aceites)
#print(total_exportadoR(0,ventas))
