"""
********************************************************************************************************
* Nombre: sopa_letras.py                                                                               *
* OBJ: Algoritmos alternativos para resolver una sopa de letras cualquiera.                            *
* Autor: David Márquez Mínguez.                                                                        *
********************************************************************************************************
"""

tabPrueba = ('h','j','k','p','u','r','e','a'),     \
            ('k','o','i','h','q','p','a','l'),     \
            ('d','a','o','o','h','t','m','o'),     \
            ('i','l','u','a','m','o','z','h'),     \
            ('a','m','u','r','o','a','l','t'),     \
            ('l','k','l','h','l','l','a','a'),     \
            ('e','o','t','o','s','p','r','a'),     \
            ('h','l','h','l','i','a','j','e')

tabPrueba1 = ('A','D','C'),   \
             ('D','D','D'),    \
             ('G','D','A')

# Array de direcciones [['Direccion', incremento filas, incremento columnas]]
direc = [['S',1,0],['N',-1,0],['O',0,-1],['E',0,1],['SE',1,1],['SO',1,-1],['NO',-1,-1],['NE',-1,1]]

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
#print(tableroPedido(nF,nC))

def pintaTablero(tablero):
    """tuplatupla]`--> nada
    OBJ: pinta tablero                             """
    for fila in tablero:
        for letra in fila: print(letra,end='\t')
        print('\n')

#Probador
pintaTablero(tabPrueba)

def busqueda(tab,pal,direc):
    """tupla[tupla], str --> nada
    OBJ: muestra las ocurrencias de palabra en todas direcciones
    PRE:todas las filas del tablero tienen=longitug"""
    nF = len(tab)    #evito pasarselo y evito acceso global
    nC = len(tab[0])
    nD = len(direc)
    tamP = len(pal)
    for d in range(nD):                # Recorremos las posibles direcciones.
        incF= direc[d][1]              # Incremento/Disminucion para las filas
        incC= direc[d][2]              # Incremento/Disminucion para las coumnas
        for f in range (nF):
            for c in range (nC):
                if pal[0]==tab[f][c]:
                    #print ('Encontrada',pal[0],'en:',f+1,',',c+1,direc[d][0])
                    puede=True
                    cont = 1 # Reseteamos el contador para cada nueva posible coincidencia.
                    if ((0<=f+incF*cont<=nF-1) and (0<=c+incC*cont<=nC-1)):# Nos aseguramos que no se sale del rango
                        while (puede and cont<tamP and (0<=f+incF*cont<=nF-1) and (0<=c+incC*cont<=nC-1)): # No se saledeltablero en ningun momento.
                            puede=puede and pal[cont]==tab[f+incF*cont][c+incC*cont]
                            #print(nF,f, incF,nC,c, incC, tab[incF][incC])
                            #if puede: print('Encontrada',pal[cont],'en:',f+incF*cont+1,',',c+incC*cont+1,direc[d][0])# +1 porque el mundo real empieza en 1
                            if(cont == tamP-1 and puede):
                                print("He encontrado la palabra:",pal,"en la posicion:",f+1,c+1,"direccion:",direc[d][0])
                            cont += 1         


#Probador
#busqueda(tabPrueba1, 'AD')
busqueda(tabPrueba, 'hola',direc)


