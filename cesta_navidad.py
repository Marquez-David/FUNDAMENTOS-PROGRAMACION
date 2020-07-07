"""
*****************************************************************************
* Nombre: cesta_navidad.py
* OBJ: Gestionar la cesta de navidad de un determinado supermercado.
*****************************************************************************
"""

from collections import namedtuple

from libInterfaz  import enteroPedido, realPedido

tFecha = namedtuple('Fecha','dia, mes, anno')

tProducto = namedtuple('Producto','id, nombre, precio, cantidad, fecha_caduc')

# Probador

fecha1 = tFecha(1,3,2018)
turron1 = tProducto(1,'turron negro',3.75,22,fecha1)
#print(turron1)

fecha2 = tFecha(28,3,2018)
turron2 = tProducto(2,'turron blanco',4.0,22,fecha2)
#print(turron2)

fecha3 = tFecha(20,3,2019)
vino1 = tProducto(3,'vino blanco',10.50,10,fecha3)
#print(vino1)

fecha4 = tFecha(20,3,2019)
vino2 = tProducto(4,'vino tinto', 20.35,10,fecha4)
#print(vino2)

fecha5 = tFecha(30,4,2018)
champ = tProducto(5,'champang',15.78,2,fecha5)
#print(champ)

productos = [turron1, turron2, vino1, vino2,champ]

cesta1 = (1,3,4) #Tupla de productos

cestas = cesta1, #Tupla de cestas
#print(cestas)

def buscar_producto(productos, num):

    """ lista(tProducto), int -> tProducto
    OBJ: Buscar un producto sabido su codigo.
    PRE: 1 <= num <= maximo id. """

    encontrado = False
    pos = 0

    while not encontrado and pos<len(productos): #No recorro toda la lista

        if(productos[pos].id == num):

            encontrado = True
            prod_encont = productos[pos]

        pos += 1

    return prod_encont

#Probador
#print(buscar_producto(productos,2))

def precio_cesta(cesta1,productos):

    """ tupla, tupla -> float
    OBJ: Calcula el precio total de una cesta.
    PRE: La cesta debe existir. """

    suma_precio = 0

    for producto in productos:

        if(producto.id in cesta1):

            suma_precio += producto.precio

    return suma_precio

#Probador
#print(precio_cesta(cesta1,productos))

def fecha_aplanada(fecha):

    """ tFecha -> int
    OBJ: Aplanar una fecha aaaammdd
    PRE: La fecha debe ser valida. """

    return fecha.anno*10000 + fecha.mes*100 + fecha.dia

#Probador
#fecha1 = tFecha(12,3,2006)
#print(fecha_aplanada(fecha1))

def es_fecha_menor(fecha1,fecha2):

    """ tFecha, tFecha -> bool
    OBJ: Si fecha1 es menor que fecha2.
    PRE: Las fechas deben ser validas. """

    menor = False

    f1 = fecha_aplanada(fecha1)
    f2 = fecha_aplanada(fecha2)

    if(f1 < f2):

        menor = True

    return menor

#Probador
#fecha1 = tFecha(2,5,2006)
#fecha2 = tFecha(3,5,2006)
#print(es_fecha_menor(fecha1,fecha2))

def antes_fecha_caducidad(productos,fecha):

    """ tupla, tFecha -> lista
    OBJ: Lista con todos los productos que caducan antes de una fecha dada.
    PRE: La fecha debe ser valida. """

    caducados = []

    for producto in productos:

        if(es_fecha_menor(producto.fecha_caduc,fecha)):

            caducados.append(producto)

    return caducados

#Probador
#fecha = tFecha(31,12,2018)
#print(antes_fecha_caducidad(productos,fecha))

def nuevo_producto(productos):

    """ tupla -> Nada
    OBJ: Introducir un nuevo producto.
    PRE: Producto valido. """

    from lib_fecha import pedir_fecha

    fechaMax = tFecha(21,12,2017)
    fechaMin = tFecha(21,12,1998)

    prod_id = len(productos) + 1
    nombre = str(input('Nombre del producto: '))
    precio = int(input('Introduce el precio: '))
    cantidad= int(input('Introduce la cantidad: '))
    fecha_caduc = pedir_fecha(fechaMin,fechaMax,'Introduce una fecha valida: ')

    nuevo_producto = tProducto(prod_id,nombre,precio,cantidad,fecha_caduc)
    
    productos.append(nuevo_producto)

#Probador
#nuevo_producto(productos)

def mayor_precio_recur(pos,productos,posM):

    """ tupla -> Nada
    OBJ: Muestr el producto con mayor precio.
    PRE: 0<=pos<=len(productos)-1. """

    if(pos == len(productos)-1):

        posM = pos

    else:

        posM = mayor_precio_recur(pos+1,productos,posM)

        if(productos[pos].precio > productos[posM].precio):

            posM = pos

    return posM

#Probador
#print(mayor_precio_recur(0,productos,0))

        

        


        

        





        

        

        

        




















