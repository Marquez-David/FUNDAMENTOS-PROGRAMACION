""" *************  servicios para manejo de dinero ************** """
# valor de las monedas editadas en el país
EDICION=(500.0,200.0,100.0,50.0,20.0,10.0,5.0,2.0,1.0,\
         0.5,0.2,0.1,0.05,0.02,0.01)
#Alternativa bonita q evita problemas redondeo: definirla en céntimos y /100 al final
#PIEZAS_M=(50000,20000,10000,5000,2000,1000,500,200,100,50,20,10,5,2,1) #en céntimos

#monedero= tupla con número (entero>0) de monedas de cada pieza editada
MON_VACIO = (0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)


def totalMonedero (monedero,edicion):
    """tupla, tupla-->float
    OBJ: valor total contenido en modenedero, con piezas de edicion
    PRE: cuantas (de cada pieza en monedero)>=0 """
    total = 0
    i = 0
    for cuantas in monedero:
        total = total+cuantas*edicion[i]
        i = i+1
    return total

#PROBADOR
monAux = (0,1,0,1,0,1,0,2,1,0,0,1,0,3,0)
'''
print(totalMonedero(monAux,EDICION), 'debe dar 265,16')
'''

    
#Me gusta más porque es más simétrica, pero valen ambas
def totalMonedero2 (monedero,edicion):
    """tupla, tupla-->float
    OBJ: valor total contenido en modenedero, con piezas de edicion
    PRE: todo i monedero[i]>=0, edicion[i]>0.0, len(monedero)=len(edicon) """
    total = 0
    for i in range(len(edicion)):
        total = total+monedero[i]*edicion[i]
    return total
'''
#PROBADOR
print(totalMonedero2(monAux,EDICION),'debe dar 265,16')
'''

def imprimirMonedero (monedero,edicion):
    """ tupla, tupla-->nada
    OBJ: imprime nº>0 de piezas en monedero de cada valor de edicion
    PRE: todo i monedero[i]>=0, edicion[i]>0.0, len(monedero)=len(edicon) """
    i = 0
    for cuantas in monedero:
        if cuantas >0:
            print (cuantas, 'de', edicion[i])
        i = i+1
'''
#PROBADOR
imprimirMonedero (monAux,EDICION)
'''

# Algunos alumnos han optado por salidas mas sofisticadas. Con buenas ideas
'''
   if n>0:
        cant=(cant-n*i)
        if n==1:                                #GUAPO EL DETALLE sig/plural
            print(n,"pieza de",i/100)           # división entera
        else:
            print(n,"piezas de",i/100)

# ó diferenciar lo que son monedas y billetes

   if cuantas >0:
      if edicion[i]>=5: print (cuantas, 'billetes de', edicion[i])
      else: print (cuantas, 'monedas de', edicion[i])

'''



#3 alternativas razonables. Deja una sola en tu biblioteca
def estaVacio(monedero):
    """ tupla, tupla-->boolean
    OBJ: True si "cuantas" de cada una de las monedas es cero
    PRE: cuantas (de cada pieza en monedero)>=0"""
    return monedero.count(0)==len(monedero)
'''
#PROBADOR
print(estaVacio(monAux), 'no vacío')
print(estaVacio(MON_VACIO),'vacío')
'''


def estaVacio2(monedero, edicion):
    """ tupla, tupla-->boolean
    OBJ: True si "cuantas" de cada una de las monedas es cero
    PRE: cuantas (de cada pieza en monedero)>=0"""
    return totalMonedero(monedero, edicion)==0

'''
#PROBADOR
print(estaVacio2(monAux,EDICION), 'no vacío')
print(estaVacio2(MON_VACIO,EDICION),'vacío')
'''

def estaVacio3(monedero):
    """ tupla-->boolean
    OBJ: True si la cuantas de cada una de las monedas es cero
    PRE:  monedero[i]>=0, MON_VACIO definido """
    return monedero==MON_VACIO



def minimoPiezas (cantidad, edicion):
    """ float, tupla -->tupla(tipo monedero)
    OBJ: minimoPiezas de "edicion" para formar cantidad
    PRE: cantidad>=0"""
    cantidad = round (cantidad*100)  # evitar imprecisiones de float
    monedero = ()                    # Creamos un monedero vacío
    for valorPieza in edicion:
        cuantas = cantidad // round (valorPieza*100)
        cantidad = cantidad% round(valorPieza*100)
        #alternativa
        #cuantas,cantidad=divmod(cantidad,round(valorPieza*100))   
        monedero = monedero+(cuantas,) # Añadimos cantidad de ésta pieza 
        # print (' valor', valorPieza, 'cuantas: ', cuantas) #trazador
    return monedero
'''
#PROBADOR
monAux = minimoPiezas(1324.58,EDICION)
print(monAux)
print(minimoPiezas(1125.23,EDICION)) 
'''

def vueltas(importe, entregado, edicion):
     """ float,float, tupla -->tupla
     OBJ: nº de piezas de cada tipo (de editadas) óptimo para dar 
     la vueta de compra por importe, cuando usuario ha entregado
     NONE si importe>entregado """
     cantidad = entregado-importe
     if cantidad >=0:
        return minimoPiezas(cantidad,edicion)
'''
#PROBADOR
vueltas(3,1,EDICION)
'''


def imprimirVueltas(importe,entregado,edicion):
     """ float,float, tupla -->nada
     OBJ: imprime nº de piezas>0 de cada tipo (de las editadas) 
     optimo para dar la vuelta de compra por importe, cuando usuario
     ha entregado.
     "Exacto" si entregado=importe.
     "Insuficiente" si entregado<importe """
     monAux = vueltas(importe, entregado, edicion)
     # print('trazador', monAux)
     if monAux is None:
         print ("insuficiente")
     elif estaVacio(monAux,edicion): print('exacto')
     else:imprimirMonedero(monAux,edicion)
                                           
'''   
#PROBADOR   
imprimirVueltas(1324.58,1000,EDICION)
'''

