"""            SOPA DE LETRAS SIN WHILE, DE MOMENTO
            4 algoritmos alternativos para la búsqueda"""

NF = 3       # Numero de filas
NC = 2       # numero de columnas

tabPrueba1 = ('A','D','C'),   \
             ('D','D','D'),    \
             ('G','D','A')

tabPrueba = ('h','j','k','p','u','r','e','a'),     \
            ('k','o','i','h','q','p','a','l'),     \
            ('d','a','l','o','h','t','m','o'),     \
            ('i','p','u','a','m','o','z','h'),     \
            ('a','m','u','r','o','a','l','t'),     \
            ('l','k','l','h','l','l','a','a'),     \
            ('e','o','t','o','s','p','r','a'),     \
            ('h','l','h','l','i','a','j','e')

tabPrueba2 = ('h','j','k','p','u','r','e','a'),     \
             ('k','o','i','h','q','p','h','l'),     \
             ('d','a','l','o','h','t','o','o'),     \
             ('i','p','u','a','m','o','l','h'),     \
             ('a','m','u','r','o','a','m','t'),     \
             ('l','k','l','h','l','l','a','a'),     \
             ('e','o','t','o','s','p','r','a'),     \
             ('h','l','h','l','i','a','j','e')

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


#PROBADOR

pintaTablero(tabPrueba2)

#pintaTablero(tabPrueba)

direc = [['S',1,0],['N',-1,0],['O',0,-1],['E',0,1],['SE',1,1],['SO',1,-1],['NO',-1,-1],['NE',-1,1]]#Demoento solo 4 posiciones,ya ire ampliando ¡¡¡FUNCIONA!!!
#direc2 =[['SE',1,1],['SO',1,-1],['NO',-1,-1],['NE',-1,1]]#Drecciones diagonales, no hacer tantes iteraciones

#de los 4 El que mas me gusta solo con for: Busco si "puede" estar la palabra
def busquedaSE3(tab,pal):
    """tupla[tupla], str --> nada
    OBJ: muestra las ocurrencias de palabra en dirección SE
    PRE:todas las filas del tablero tienen=longitug"""
    nF = len(tab)    #evito pasarselo y evito acceso global
    nC = len(tab[0])
    tamP = len(pal)
    cont = 1
    for f in range (nF):
        for c in range (nC):
            if pal[0]==tab[f][c]:# Encontramos la 'h'
                print ('Encontrada',pal[0],'en:',f+1,',',c+1,)
                incF=1                          # Incremento para las filas
                incC=1                          # Incremento para las coumnas
                puede=True
                cont = 1 # Reseteamos el valor para cada nueva aparicion
                if (nF-f>=tamP and nC-c>=tamP):    # Nos aseguramos que no se va a salir del rango
                    while puede and cont<tamP: 
                        puede=puede and pal[cont]==tab[f+incF*cont][c+incC*cont]
                       # print(nF,f, incF,nC,c, incC, tab[incF][incC])
                        if puede: print('Encontrada',pal[cont],'en:',f+incF*cont+1,',',c+incC*cont+1,'SE')# +1 porque el mundo real empieza en 1
                        cont += 1
    
#Probador:
#print('tercero')
#busquedaSE3(tabPrueba, 'hola')

#generalizamos a todas las direcciones
def busqueda(tab,pal,direc):
    """tupla[tupla], str --> nada
    OBJ: muestra las ocurrencias de palabra en todas direcciones
    PRE:todas las filas del tablero tienen=longitug"""
    nF = len(tab)    #evito pasarselo y evito acceso global
    nC = len(tab[0])
    nD = len(direc)
    tamP = len(pal)
    for d in range(nD): #Se repetira tantas veces como posiciones haya que buscar.
        incF=direc[d][1] #Incremento para las filas
        incC=direc[d][2] #Incremento para las columnas
        for f in range (nF):# Recorremos las filas.
            for c in range (nC):# Recoremos las columnas.
                if pal[0]==tab[f][c]:# Encontramos la 'h'
                    #print ('Encontrada',pal[0],'en:',f+1,',',c+1,direc[d][0])
                    puede=True
                    cont = 1 # Reseteamos el valor para cada nueva aparicion
                    if ((0<=f+incF*cont<=nF-1) and (0<=c+incC*cont<=nC-1)):    # Nos aseguramos que no se va a salir del rango
                        while (puede and cont<tamP and (0<=f+incF*cont<=nF-1) and (0<=c+incC*cont<=nC-1)): 
                            puede=puede and pal[cont]==tab[f+incF*cont][c+incC*cont]
                            #print(nF,f, incF,nC,c, incC, tab[incF][incC])
                            #if puede:
                                #print('Encontrada',pal[cont],'en:',f+incF*cont+1,',',c+incC*cont+1,direc[d][0])# +1 porque el mundo real empieza en 1
                            if(cont == tamP-1 and puede):
                                print("He encontrado la palabra:",pal,"en la posicion:",f+1,c+1,"direccion:",direc[d][0])
                            cont += 1
                        
#Probador

#busqueda(tabPrueba1, 'AD',direc)
busqueda(tabPrueba2, 'hola',direc)

