"""
******************************************************************************
* Nombre: sopa_letras.py
* OBJ: Dos algoritmo que abordan la resolucion de una sopa.
* Autor: David Márquez Míngez.
******************************************************************************
"""

NF = 3       # Numero de filas
NC = 2       # numero de columnas 

tabPrueba = ('h','j','k','p','u','r','e','a'),     \
            ('k','o','i','h','q','p','a','l'),     \
            ('d','a','l','o','h','t','m','o'),     \
            ('i','p','u','a','m','o','z','h'),     \
            ('a','m','u','r','o','a','l','t'),     \
            ('l','k','l','h','l','l','a','a'),     \
            ('e','o','t','o','s','p','r','a'),     \
            ('h','l','h','l','i','a','j','e')

tabPrueba1 = ('A','D','C'),   \
             ('D','D','D'),    \
             ('G','D','A')

def tableroPedido(nF, nC):
    """int,int--> tupla[tupla]
    OBJ: pide al usuario un tablero de nF filas por nC columnas
    PRE: nF, nC>=0                                               """
    tablero = tuple()
    for i in range(nF):          #cada fila
        fila = tuple()
        for j in range(nC):     # cada columna
            letra = input(str(i)+','+str(j)+': ')
            fila +=(letra,)
        tablero=tablero+(fila,)
    return tablero

#Probador
#print(tableroPedido(nF,nC)

def pintaTablero(tablero):
    """tuplatupla]`--> nada
    OBJ: pinta tablero                             """
    for fila in tablero:
        for letra in fila: print(letra,end='\t')
        print('\n')


#Probador

pintaTablero(tabPrueba)

#de los 4 El que mas me gusta solo con for: Busco si "puede" estar la palabra
def busquedaSE3(tab,pal):
    """tupla[tupla], str --> nada
    OBJ: muestra las ocurrencias de palabra en dirección SE
    PRE:todas las filas del tablero tienen=longitug"""
    nF = len(tab)    #evito pasarselo y evito acceso global
    nC = len(tab[0])
    tamP = len(pal) 
    for f in range (nF):
        for c in range (nC):
            if pal[0]==tab[f][c]:
                print ('encontrada', pal[0], 'en', f,',',c)
                incF=1                          # +1 porque estamos buscndo en SE
                incC=1                          # +1porque busacmos en SE
                puede=True
                if nF-f>=tamP and nC-c>=tamP:    #Nos aseguramos que no se sale del rango
                    for k in range(1,tamP):
                        puede=puede and pal[k]==tab[f+incF*k][c+incC*k]
                        #print(nF,f, posF,nC,c, posC, tab[posF][posC])
                    if puede: print('Encontrada',pal,'en:',f+1,c+1,'sentido %2s'%'SE')#
                     #+1 porque el mundo real empieza en 1
#Probador:
#print('tercero')
#busquedaSE3(tabPrueba, 'hola')

# Conseguido, mas eficiente que el anterior, aun así, en cuanto "no puede"
# ¿para qué seguir buscando? Ahora ya disponemos del while, reescríbelo

#mas eficiente, con while que con for... en cuanto una letra no encaja se sale
def busquedaSE5(tab,pal):
    """tupla[tupla], str --> nada
    OBJ: muestra las ocurrencias de palabra en dirección SE
    PRE:todas las filas del tablero tienen=longitug"""
    nF = len(tab)   #Cuantas filas 
    nC = len(tab[0])#Cuantas columnas
    tamP = len(pal)
    for f in range(nF): #Recorremos todas las filas
        for c in range(nC): #Recorremos todaslas columnas
            if(pal[0] == tab[f][c]): #Encontramosla 'h'
                #print('Encontrada',pal[0],'en:',f+1,',',c+1)# +1 para acercarnos a la realidad
                incF = 1
                incC = 1
                puede = True
                cont = 1 #Reseteamos e contador en cada posible encuentro
                if(nF-f>=tamP and nC-c>=tamP): #Nos aseguramos que no se sale del rango
                    while(puede and cont<tamP):
                        puede = puede and pal[cont]==tab[f+incF*cont][c+incC*cont]
                        #if(puede): print('Encontrada',pal[cont],'en:',f+incF*cont+1,c+incC*cont+1)
                            #+1 para acercarnos a la realidad
                        if (cont == tamP-1 and puede):
                            print("He encontrado la palabra",pal,f+1,c+1,"en direccion SE")
                        cont = cont + 1              
#Probador:
#print('quinta')
busquedaSE5(tabPrueba, 'hola')
