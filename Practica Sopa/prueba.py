tabPrueba = ('h','j','k','p','u','r','e','a'),     \
            ('k','o','i','h','q','p','a','l'),     \
            ('d','a','l','o','h','t','m','o'),     \
            ('i','p','u','a','m','o','z','h'),     \
            ('a','m','u','r','o','a','l','t'),     \
            ('l','k','l','h','l','l','a','a'),     \
            ('e','o','t','o','s','p','r','a'),     \
            ('h','l','h','l','i','a','j','e')

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
                print ('Encontrada',pal[0],'en:',f,',',c)
                incF=1                          # Incremento para las filas
                incC=1                          # Incremento para las coumnas
                puede=True
                cont = 1 # Reseteamos el valor para cada nueva aparicion
                if (nF-f>=tamP and nC-c>=tamP):    # Nos aseguramos que no se va a salir del rango
                    while puede and cont<tamP: 
                        puede=puede and pal[cont]==tab[f+incF*cont][c+incC*cont]
                       # print(nF,f, incF,nC,c, incC, tab[incF][incC])
                        if puede: print('Encontrada',pal[cont],'en:',f+incF*cont,',',c+incC*cont)#
                        cont += 1
                     #+1 porque el mundo real empieza en 1
#Probador:
#print('tercero')
busquedaSE3(tabPrueba, 'hola')
