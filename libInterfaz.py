"""********************************************************************
*                      biblioteca: libInterfaz                        *
*OBJ: agrupa facilidades para la interfaz de usuario                  *
*     centrarRotulo (rotulo,signo,tamVentana=76)                      *
*     enteroPedido (min,max,msg)                                      *
*     realPedido (min,max, msg)                                       *
********************************************************************"""

def centrarRotulo (rotulo,signo,tamVentana=76):
    """str,str,[int]-->[]
    OBJ: centra rótulo, subrayado con signo en ventana de tamaño 
        indicado,+ linea encima y debajo
    PRE: len(rotulo)<=tamVentana<=150"""
    tam = len(rotulo)
    lado = (tamVentana-tam)//2-1 #-1 xq print deja blanco entre argum
    print ()
    print(' '*lado,rotulo)
    print(' '*lado,'='*tam)
    print()

#centrarRotulo ('Aplicación de combinatoria','*') 

def enteroPedido (min,max, msg):
    """ int,int, str,str-->int
    OBJ: pide entero a usuario entre min y max, mostrando msg
    PRE: min<=max                                           """

    pedir = True
    while  pedir or not (min<=n<=max):
        try:
            n = int(input(msg))
            pedir = False
        except:print('debe ser un entero. ', end='')        
    return n
'''
#Probador
min = 1
max = 12
print(enteroPedido(min,max,'mes entre '+str(min)+' y '+str(max)+': '))
'''

def realPedido (min,max,msg):
    """float, float, str -->float
    OBJ: pide real a usuario, entre min y max, mostrando msg    """

    pedir = True
    while  pedir or not (min<=n<=max):
        try:
            n = float(input(msg))
            pedir = False
        except:print('debe ser un real. ', end='')
            
    return n
'''
print(realPedido(min,max,'real entre '+str(min)+' y '+str(max)+': '))
'''
