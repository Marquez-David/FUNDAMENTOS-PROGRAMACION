"""
****************************************************************************
* Nombre: lib_fecha.py
* OBJ: libreria que incluye funciones de fecha.
****************************************************************************
"""

from collections import namedtuple

diasMes = (31,29,31,30,31,30,31,31,30,31,30,31)

letraMes = ('Enero', 'Febrero','Marzo','Abril','Mayo','Junio','Julio',
            'Agosto','Septiembre','Octubre','Noviembre','Diciembre')

tFecha = namedtuple('Fecha', 'dia, mes, anno')

tFechas = namedtuple('Fechas','dias, meses, annos')

tTiempo = namedtuple('Tiempo','hora, min, seg')

def cuantos_dias(mes):

    """ int -> int
    OBJ: Cuantos dis tiene un mes.
    PRE: 1<=mes<=12. """

    return diasMes[mes-1]

#print(cuantos_dias(2))

def es_bisiesto(anno):

    """ int -> bool
    OBJ: Si un año es bisiesto.
    PRE: anno>1582. """

    bisiesto = False

    if((anno%4 == 0) and (anno%100 != 0 or anno%400 == 0)):

        bisiesto = True

    return bisiesto

#print(es_bisiesto(2016))

def es_fecha_valida(fecha):

    """ tFecha -> bool
    OBJ: Si es valida una fecha.
    PRE: f.anno > 1582. """

    if(not(es_bisiesto(fecha.anno)) and fecha.mes == 2):

        uD = 28

    else:

        uD = cuantos_dias(fecha.mes)

    return 1<= fecha.dia <= uD and 1<= fecha.mes <= 12

#fecha = tFecha(19,3,2015)
#print(es_fecha_valida(fecha))
#fecha = tFecha(31,2,2016)
#print(es_fecha_valida(fecha))

def fecha_aplanada(fecha):

    """ tFecha -> int
    OBJ: Aplanar una fecha dada.
    PRE: es fecha valida. """

    return fecha.anno*10000 + fecha.mes*100 + fecha.dia


#fecha = tFecha(12,5,2005)
#print(fecha_aplanada(fecha))

def ordenadas(fecha1,fecha2):

    """ tFecha,tFecha -> tFecha, tFecha
    OBJ: Orden demenor a mayor fecha1 y fecha2.
    PRE: Fecha1 fecha2 deben ser fechas validas. """

    fecha_aplanada(fecha1)

    fecha_aplanada(fecha2)

    if(fecha1 > fecha2):

        ordenada = (fecha2, fecha1)

    else:

        ordenada = fecha1, fecha2

    return ordenada

#fecha1 = tFecha(13,5,2007)
#fecha2 = tFecha(14,5,2007)
#print(ordenadas(fecha1,fecha2))

def pedir_fecha(fechaMin,fechaMax,msg):

    """ Nada -> tFecha
    OBJ: Pide feccha al usuarrio hasta que introduzca una valida. """

    from libInterfaz import enteroPedido

    dia = enteroPedido(1, 31,'Introduce dia valido')

    mes = enteroPedido(1, 12,'Introduce un mes valido')

    anno = enteroPedido(fechaMin.anno,fechaMax.anno,'Introduceun año valido')

    fecha = tFecha(dia,mes,anno)

    valida = es_fecha_valida(fecha)

    while not valida:

        dia = enteroPedido(1, 31,'Introduce dia valido')

        mes = enteroPedido(1, 12,'Introduce un mes valido')

        anno = enteroPedido(fechaMin.anno,fechaMax.anno,'Introduceun año valido')

        fecha = tFecha(dia,mes,anno)

        valida = es_fecha_valida(fecha)

    return fecha

#fechaMax = tFecha(21,12,2017)
#fechaMin = tFecha(21,12,1998)
#print(pedir_fecha(fechaMin, fechaMax,'Introduce fecha valida'))

def imprimir_fecha_separador(fecha):

    """ tFecha -> Nada
    OBJ: Imprime fecha por pantalla separa por barras.
    PRE: fecha debe ser valida. """

    return fecha.dia,'/',fecha.mes,'/',fecha.anno

fecha = tFecha(12,4,2008)
print(imprimir_fecha_separador(fecha))

def mes_letras(mes):

    """ int -> str
    OBJ: Devuelve un mes en letras.
    PRE: Mes debe ser valido. """

    return letraMes[mes-1] #Empiezan en 0

def imprimir_fecha_letras(fecha):

    """ tFecha -> Nada
    OBJ: Imprime una fecha con sepradores en letras 25 de Junio de 2005.
    PRE: La fecha debe ser valida. """

    print(fecha.dia,'de',mes_letras(fecha.mes),'de',fecha.anno)
    
#fecha = tFecha(12,10,1998)
#imprimir_fecha_letras(fecha)

def cuantos_bisiestos(fecha1,fecha2):

    """ tFecha, tFecha -> int
    OBJ: Devuelve cuantos años bisiestos hay entre dos fechas.
    PRE: Las fechas deben ser validas. """

    bisiestos = 0

    for anno in range(fecha1.anno,fecha2.anno):

        if(es_bisiesto(anno)):

            bisiestos += 1

    return bisiestos

#fecha1 = tFecha(1,3,2005)
#fecha2 = tFecha(1,4,2017)
#print(cuantos_bisiestos(fecha1,fecha2))

def dias_entre_fechas(fecha1,fecha2):

    """ tFecha, tFecha -> int
    OBJ: Devuelve los dias transcurridos entre dos fechas.
    PRE: Las fechas deben ser validas. """

    dias_tot = 0

    dias_tot += (fecha2.anno - fecha1.anno)*365 + cuantos_bisiestos(fecha1,fecha2) #Dias entre años contando años bisiestos

    dias_tot += cuantos_dias(fecha1.mes) - fecha1.dia #Dias que quedan para terminar mes

    dias_tot += fecha2.dia #Dias que sobran al mes de la segunda fecha

    for mes in range(fecha1.mes+1,fecha2.mes): #Dias entre meses

        dias_tot += cuantos_dias(mes)

    return dias_tot

#fecha1 = tFecha(1,3,1998)
#fecha2 = tFecha(30,8,2017)
#print(dias_entre_fechas(fecha1,fecha2))

def fecha_en_dias(fecha,n):

    """ tFecha, int -> tFecha
    OBJ: Nueva fecha n dias despues de la fecha dada.
    PRE: La fecha debe ser valida y 'dias'>= 0. """

    dia = fecha.dia + n
    mes = fecha.mes
    anno = fecha.anno

    while(dia > cuantos_dias(fecha.mes)):

        dia -= cuantos_dias(fecha.mes)
        mes += 1

    while(mes > 12):

        mes -= 12
        anno += 1

    fecha_nueva = tFecha(dia,mes,anno)

    return fecha_nueva

#fecha = tFecha(2,11,2017)
#print(fecha_en_dias(fecha,65))

def dia_sig_fecha(fecha):

    """ tFecha -> tFecha
    OBJ: Dia siguiente a una fecha dada.
    PRE: La fecha debe ser valida. """

    return fecha_en_dias(fecha,1)

#fecha = tFecha(1,1,2010)
#print(dia_sig_fecha(fecha))

def tiempo_entre_fechas(fecha1,fecha2):

    """ tFecha, tFecha -> tFechas
    OBJ: Tiempo transcurrido  entre dos fechas.
    PRE: Las fechas deben ser validas. """

    dias = dias_entre_fechas(fecha1,fecha2)
    meses = 0
    annos = 0

    print(dias)

    while(dias > cuantos_dias(fecha1.mes)):

        dias -= cuantos_dias(fecha1.mes)
        meses += 1

    while (meses > 12):

        meses-=12
        annos+= 1

    fechas = tFechas(dias,meses,annos)

    return fechas

#fecha1 = tFecha(27,10,2005)
#fecha2 = tFecha(23,9,2013)
#print(tiempo_entre_fechas(fecha1,fecha2))

def tiempo_entre_horas(tiempo1,tiempo2):

    """ tTiempo, tTiempo -> tTiempo
    OBJ: Tiempo transcurrido entre dos horas expresado en h:m:s
    PRE: El tiempo debe ser valido. """

    if(tiempo2.hora < tiempo1.hora):

        tiempo2.hora += 24

    horas = tiempo2.hora - tiempo1.hora

    if(tiempo2.min < tiempo1.min):

        horas -= 1

        minutos = 60 - tiempo1.min + tiempo2.min

    else:

        minutos = tiempo2.min - tiempo1.min

    if(tiempo2.seg < tiempo1.seg):

        minutos -= 1

        segundos = 60 - tiempo1.seg + tiempo2.seg

    else:

        segundos = tiempo2.seg - tiempo1.seg

    tiempo_entre = tTiempo(horas,minutos,segundos)

    return tiempo_entre

#tiempo1 = tTiempo(13,50,6)
#tiempo2 = tTiempo(18,59,50)
#print(tiempo_entre_horas(tiempo1,tiempo2))

    
        



                         
                     

        

    


        

    
