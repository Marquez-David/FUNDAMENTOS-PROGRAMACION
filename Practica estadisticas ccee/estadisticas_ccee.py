"""
*****************************************************************************
* Nombre: estadisticas_ccee                                                 *
* OBJ: Construir una tabla con las estadisticas de la CCEE                  *
* Autor: David Márquez Mínguez                                              *
*****************************************************************************
"""

NOMBRE_PAISES = ('Alemania', 'Francia','Reino Unido', 'Italia', 'España')

pib = (3144050, 2228857, 2393134, 1680523, 1118522)

poblacion = (82605000, 64770000, 65893000, 60721000, 46427000)

poblacion_duplicada = (82605000, 64770000, 65893000, 60721000,
                       46427000,82605000, 64770000, 65893000, 60721000, 46427000)

P = 20000.0 #Limite de poblacion

Q = 1500000.0 #Limite de pib

def listar_paises(NOMBRE_PAISES):

    """ tupla --> Nada
    OBJ: Lista los 5 primeross paises de la CCEE.
    PRE: Nada. """

    for paises in NOMBRE_PAISES:

        print(paises)

#Probador
#listar_paises(NOMBRE_PAISES)

def pais_en_pos(NOMBRE_PAISES,pos):

    """ tupla, int --> str
    OBJ: Devuelve el pais que esta en pos.
    PRE: pos debe ser un int, 1 <= pos <= 5. """

    nombre = ''

    for i in range(1,len(NOMBRE_PAISES)+1):

        if(i == pos):

            nombre = NOMBRE_PAISES[pos-1]

    return nombre

#Probador
#pais_en_pos(NOMBRE_PAISES, 1)
#pais_en_pos(NOMBRE_PAISES, 3)
#pais_en_pos(NOMBRE_PAISES, 5)

def esta_primeros(NOMBRE_PAISES,pais):

    """ tupla, str --> bool
    OBJ: Determina si un pais esta entre los 5 primeros.
    PRE: Nada. """

    nP = len(NOMBRE_PAISES)

    esta = False

    cont = 0

    while  not(esta) and cont<nP: #Sabremos por donde sale por evaluacion perezosa.

        if(NOMBRE_PAISES[cont]==pais):

            esta=True

        cont += 1

    return esta

#Probador
#esta_primeros(NOMBRE_PAISES,"España")
#esta_primeros(NOMBRE_PAISES,"Holanda")

def mas_poblacion(poblacion,num_personas):

    """ tupla,float --> int
    OBJ: Cuantos paises tiene mas poblacion que num_personas.
    PRE: num_personas >= 0. """

    cuantos = 0

    for personas in poblacion:

        if(personas > num_personas):

            cuantos = cuantos +1

    return cuantos

#Probador
#mas_poblacion(poblacion,85605000)
#mas_poblacion(poblacion,60605000)

def poblacion_total(poblacion):

    """ tupla --> int
    OBJ: Devuelve la poblacion total de los paises.
    PRE: Nada. """

    total = 0

    for personas in poblacion:

        total = total + personas

    return total

#Probador
#poblacion_total(poblacion)
#pobl_total = poblacion_total(poblacion)

def imprimir_tabla(NOMBRE_PAISES,poblacion,porcent_pobl,pib):

    """ tupla, tupla --> Nada
    OBJ: Imprime una tabla con el niombre de cada pais y su poblacion.
    PRE: Nada. """

    nP = len(NOMBRE_PAISES) #Numero de paises, evito accesso global

    print('listado de paises')
    print('================================================================')
    print('PAIS           POBLACION          %POBLACION              pib')
    print()

    for i in range(nP):

        tamP = len(NOMBRE_PAISES[i])

        print(NOMBRE_PAISES[i],' '*(13-tamP),poblacion[i],' '*12,porcent_pobl[i],'%',' '*10,pib[i])

#Probador
#imprimir_tabla(NOMBRE_PAISES,poblacion,porcent_pobl,pib)

def porcentaje_poblacion(poblacion):

    """ tupla --> lista
    OBJ: Crea una tupla con el  porcentaje de pobacion de cada pais.
    PRE: Nada. """

    pobl_total = poblacion_total(poblacion)

    porcent_pobl = []

    for habitantes in poblacion:

        porcent_pobl.append(round(habitantes*100/pobl_total,2))

    return porcent_pobl

#Probador
porcent_pobl = porcentaje_poblacion(poblacion)

def pib_total(pib):

    """ tupla --> float
    OBJ: Calcula el pib total de los paises de la cee.
    PRE: Nada. """

    total = 0

    for riqueza in pib:

        total += riqueza

    return total

#Probador
#riqueza_total = pib_total(pib)

def renta_percapita_media(riqueza_total,pib):

    """ tupla, tupla --> float
    OBJ: Calcula la renta percapita media de la CEE.
    PRE: La renta va en Millones. """

    return riqueza_total/len(pib)

#Probador
#renta_percapita_media(riqueza_total,pib)

def hay_menos_poblacion(poblacion,num_personas):

    """tupla,int --> bool
    OBJ: Recorre tupl hasta un pais con menos poblacion que una dada.
    PRE: La poblacion dada debe ser un numero valido. """

    es_menor = False

    nP = len(poblacion)

    cont = 0

    while not(es_menor) and cont<nP:

        if(poblacion[cont]<num_personas):

            es_menor = True

        cont += 1

    return es_menor

#Probador
#menos_poblacion(poblacion,85000000)
#menos_poblacion(poblacion,45000000)


#Resolvemos el mismo prblema anterior pero con la tecnica del CENTINELA
def hay_menos_poblacion_2(poblacion_duplicada,num_personas):

    """ tupla, int --> bool
    OBJ: Recorre latupla hasta un pais con menor poblacion que la dada
    PRE: La poblacion debe ser un numero valido. """

    poblacion_duplicada+=(num_personas,)

    pos = 0

    esta = True

    while num_personas < poblacion_duplicada[pos]:

        pos += 1

    if(pos == len(poblacion_duplicada)-1):

        esta = False

    return esta

#Probador
#hay_menos_poblacion_2(poblacion_duplicada,85000000)
#hay_menos_poblacion_2(poblacion_duplicada,45000000)

def aniadir_paises():

    """ Nada --> tupla, tupla, tupla.
    OBJ: Crea una tupla con los paises añadidos por el usuario
    PRE:Los paises y valores introducidos deben ser validos. """

    global NOMBRE_PAISES,poblacion,pib #Modificar varibles globales

    CENTINELA = 'fin'

    pais = str(input("Nombre pais(fin para terminar): "))

    while pais != CENTINELA:

        pib_intr = float(input("Introduce el pid del pais: "))

        if(pib_intr < Q):

            print("Peligro de consanguinidad. ")

        pib += (pib_intr, )

        habitantes = int(input("Introduce los habitantes del pais: "))

        if(habitantes < P):

            print("Peligro de consanguinidad. ")

        poblacion += (habitantes, )

        NOMBRE_PAISES += (pais, )

        pais = str(input("Nombre pais(fin para terminar): "))

    return NOMBRE_PAISES,poblacion,pib

#Probador
#aniadir_paises(NOMBRE_PAISES,pib,poblacion)

def mayor_pib(pib,NOMBRE_PAISES):

    """ tupla,tupla --> int
    OBJ: Cuantos paises tienen mas de la mitad del pib del primer pais.
    PRE: Nada. """

    pib_primer = pib[0]

    cont = -1

    print("Los paises que tinen mas de la mitad de pib que",NOMBRE_PAISES[0],"son:")

    for dinero in pib:

        if(dinero > pib_primer/2 ):

            cont += 1

            print(NOMBRE_PAISES[cont], end='. ')

    return cont

#Probador
#mayor_pib(pib,NOMBRE_PAISES)

datos = aniadir_paises()
porcent_pobl = porcentaje_poblacion(poblacion)
imprimir_tabla(datos[0],datos[1],porcent_pobl,datos[2])
    

    

    



    

        





