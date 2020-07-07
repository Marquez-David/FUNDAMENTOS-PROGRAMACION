""" Estadísticas de la CEE"""
#1
PAISES= ('Alemania', 'Francia', 'Reino Unido', 'Italia', 'España') 
#21
P=20000.0                  #no te olvides de poner los decimales
Q=1500000
#2

def lista (tupla):  #he generalizado el nombre, xq vale para cualquier tupla
    """tupla (elementos)-->Nada
    OBJ: Listado de elementos de una tupla"""   #no hay PRE en este subp
    
    for elemento in tupla:
        print(elemento)
        
#3
#PROBADOR
lista (PAISES)

#4
def elemento (tupla, pos):
    """tupla, int-->elemento
    OBJ: devuelve el elemento en pos (empezando a contar por el 1)
    PRE: 1=<pos=<len(tupla)"""
    return tupla(pos-1)

#5
def estaEnTuplaElemento(tupla,elemento):
    """tupla,str-->bool   #realmente, vale para cualquier tipo de elementos de la tupla
    OBJ: Está el elemento en la tupla?  """
    return elemento in tupla

#PROBADOR
print('España esta', estaEnTuplaElemento(PAISES, 'España'))
print('Zambia está', estaEnTuplaElemento(PAISES, 'Zambia'))


#6
pibS=(3144050,2228857,2393134,1680523,1118522)  #la S para aclarar que es plural
poblaciones=(82605000,64770000,65893000,60721000,46427000)

#7
def cuantosMasTupla(tupla,cantidad):
    """tupla(float), float-->int           #de hecho, cualquiera que sea el tipo
                                           #de los elementos de la tupla  
    OBJ: cuantos tienen mas que cantidad"""
    cont=0
    for elemento in tupla:
        if elemento >cantidad: cont=cont+1
    return cont

#PROBADOR
print('hay ',cuantosMasTupla(poblaciones, 100000), 'con mas de 100000')

#8
def total (tupla):
    """tupla(float/int)-->float/int
    OBJ: suma total de los elementos de la tupla"""
    suma=0.0
    for elemento in tupla:
        suma+=elemento
    return suma

#PROBADOR
print (total(poblaciones))

#9
def pintaTabla(nombres, pobl):
    """tupla,tupla-->Nada
    OBJ: pintar tabla de población
    PRE: len(nombre)==len(pobl)"""

    print( '  PAIS        POBLACIÓN')
    for i in range (len(nombres)):
        print('%11s %10d' %(nombres[i], pobl[i]))

#PROBADOR
pintaTabla(PAISES, poblaciones)

#10
def pintaTabla(nombres, pobl):
    """tupla,tupla-->Nada
    OBJ: pintar tabla de población
    PRE: len(nombre)==len(pobl)"""

    print( '  PAIS        POBLACIÓN')
    for i in range (len(nombres)):
        print(nombres[i],' '*(11-len(nombres[i])), '%10d' %(pobl[i]))

#PROBADOR
#pintaTabla(PAISES, poblaciones)


#11 al 13

def pintaTabla3(nombres, pobl,pibS):
    """tupla,tupla-->Nada
    OBJ: pintar tabla de población, porcentajey PIB
    PRE: len(nombre)==len(pobl)"""

    print( '  PAIS        POBLACIÓN    %POBLAC       pib' )
    tot=total(pobl)
    print(tot)
    for i in range (len(nombres)):
        print(nombres[i],' '*(11-len(nombres[i])), \
              '%10d %9.2f %13.2f' %(pobl[i],pobl[i]/tot*100, pibS[i]))

#PROBADOR

print(13)
pintaTabla3(PAISES, poblaciones, pibS)


#14
def rentaMedia(pibS, pobl):
    """tupla, tupla-->float
    OBJ: renta percápita media de la CC
    PRE: len(pibS)=len(pobl)"""
    return total(pibS)*1000000/total(pobl)

#PROBADOR
print('renta media', rentaMedia(pibS,poblaciones))

#15 como el 5, pero sin operador in
def estaEnTuplaElemento(tupla,elemento):
    """tupla,str-->bool   #realmente, vale para cualquier tipo de elementos de la tupla
    OBJ: Está el elemento en la tupla?  """
    pos=0
    while pos<len(tupla) and tupla[pos]!=elemento:
        pos+=1
    
    return pos<len(tupla)
'''
#PROBADOR
print('España esta', estaEnTuplaElemento(PAISES, 'España'))
print('Zambia está', estaEnTuplaElemento(PAISES, 'Zambia'))

'''
#16
def hayElementoMenor(tupla, valor):
    """tupla(int),int --> bool
    OBJ: ¿hay algún elemento en tupla menor de valor?"""
    
    pos=0
    while pos<len(tupla) and tupla[pos]>=valor: pos+=1
    return pos<len(tupla)


#17

poblaLista=[82605000,64770000,65893000,60721000,46427000]

def hayElementoMenorLista(lista, valor):
    """lista(int),int --> bool
    OBJ: ¿hay algún elemento en lista menor de valor?"""
    
    lista.append(valor-1)
    pos=0
    while lista[pos]>=valor: pos+=1
    lista.pop()                        #OJO retirar el elemento añadido, ejercicio 17
    return pos<=len(lista)
   
#PROBADOR
print('hay < 1000', hayElementoMenorLista(poblaLista, 1000))
print('hay < 1000000', hayElementoMenorLista(poblaLista, 1000000))

print(poblaLista)

#18
'''no, las tuplas son inmutables, como las cambio con asignación
total de la variable, no hay efectos laterales

append es un método de lista, y es la forma natural de añadir elemento a lista
si no lo has usado en tu propuesta de solución, hazlo ahora y
comprueba lo que ocurre

La opción de coiar a lista a una auxilir no es buena idea.La técnica del centilea
se tiene ventaja cuando los arrays son muy grandes y compense el tiempo perdido
en hacer, digamos mil preguntas con el de dar un alta y una baja al elemento


'''


    
#19

def paisesPedidos():
    """nada-->tupla(string)
    OBJ: pide al usuario el nombre de paises hasta que escriba "fin" """
   
    PAISES=tuple()
    pais=input('introduzca nombre del país, o "fin" para acabar: ')
    while pais!='fin':  #(0-n)+1
        PAISES+=(pais,)
        pais=input('introduzca nombre del país, o "fin" para acabar: ')
 
    return PAISES
#PROBADOR
#print(paisesPedidos())


''' elijo este algoritmo xq es parecido a lo que harias en otros
lenguajes. En Python, puedes crear una lista, append elementos
y finalmente convertirla a tupla, como en el subprog siguente



def tupla():
    """***************************************************
    * -> tuple                                           *
    * OBJ: Crea una tupla con los elementos introducidos.*
    * por: Ignacio López García                          *
    ***************************************************"""

    lista = []

    elemento = input("Introduce un nombre, por favor:\t")
    while(elemento != "fin"):
        lista.append(elemento)
        elemento = input("Introduce un nombre, por favor:\t")
    return (tuple(lista))
'''
#y... Ya que estamos aquí, ¿cual de las dos alternativas
# es mas eficiente en Python???

#20

def paisesPedidos1():
    """nada-->tupla(string), tupla(int),tupla(int)
    OBJ: pide al usuario los datos de los paises hasta que escriba "fin" """
    PAISES=tuple()
    pibS= tuple()
    poblaciones=tuple()
    pais=input('introduzca nombre del país: ')
    while pais!='fin':
        try: 
            ibp=float(input('producto int bruto: '))
            pibS+=(ibp,)
            error=0
        except:
            error=1
            print('pib debe ser un número real')
        if error==0: 
           try:
              p=int(input('num de habitantes: '))
              poblaciones+=(p,)
           except:
            error=1
            print('poblacion debe ser un número entero')
        if error==0:
            PAISES+=(pais,)
            pais=input('introduzca nombre del país: ')
        
    return PAISES, pibS, poblaciones
'''
#PROBADOR
print(paisesPedidos1())
'''

#22
#paises, pibS, poblaciones =paisesPedidos()
#rpr: me niego a hacer las pruebas metiendo datos.
#Cuando lo tenga quito # de la inst anterior
pintaTabla3(PAISES, poblaciones, pibS)
print('TOTAL', ' '*(11-5),  '%10d %23.2f' %(total(poblaciones),total(pibS)))
print()
if hayElementoMenor(poblaciones, P): print('no ', end='')
print('hay riesgo de consanguinidad')
if hayElementoMenor(pibS, Q): print('no ', end='')
print('hay riesgo de pobreza')

print(cuantosMasTupla(pibS,pibS[0]/2),'paises tienen pibS mayor que',PAISES[0])

        
