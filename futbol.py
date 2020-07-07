"""
********************************************************************************
* Nombre: futbol.py
* OBJ: Gestion jugadores de la FEF.
******************************************************************************
"""

from collections import namedtuple

tJugador = namedtuple('Jugador','nombre, pos_campo, equipo, num_goles')

posicion = ('defensa','medio','delantero')

#Probador

jugador1 = tJugador('Messi',posicion[2],'FCBarcelona',35)
#print(jugador1)

jugador2 = tJugador('Ronaldo',posicion[1],'RealMadrid',10)
#print(jugador2)

jugador3 = tJugador('Rodrigo',posicion[2],'Valencia',15)
#print(jugador2)

jugador4 = tJugador('Muriel',posicion[1],'Sevilla',40)
#print(jugador4)

jugador5 = tJugador('Suarez',posicion[2],'FCBarcelona',60)
#print(jugador5)

jugadores = [jugador1, jugador2, jugador3,jugador4,jugador5]

def mejores_delanteros(jugadores,posicion,goles_min): #ITERATIVO

    """ tupla(tJugador) -> lista
    OBJ: Devuelve una lista con los candidatos al mejor delantero
    PRE: Nada. """

    candidatos = []

    for jugador in jugadores:

        if(jugador.num_goles >= goles_min and jugador.pos_campo == posicion[2]):

            candid_goleador = tJugador(jugador.nombre,jugador.pos_campo,
                                       jugador.equipo,jugador.num_goles)

            candidatos.append(candid_goleador)

    return candidatos

#Probador
print(mejores_delanteros(jugadores,posicion,20))

def mejores_delanterosR(pos,jugadores,goles_min,posicion):

    """ int, tupl(tJugador) -> lista
    OBJ: Devuelve una lista con los candidatos al mejor delantero.
    PRE: 0<= pos <= len(jugadores)-1. """

    candid_goleador = []

    if(pos == len(jugadores)-1):

        if(jugadores[pos].num_goles >= goles_min and jugadores[pos].pos_campo == posicion[2]):

            candid_goleador.append(jugadores[pos])

    else:

        #candid_goleador += mejores_delanterosR(pos+1,jugadores,goles_min,posicion)

        if(jugadores[pos].num_goles >= goles_min and jugadores[pos].pos_campo == posicion[2]):

            candid_goleador.append(jugadores[pos])

        candid_goleador += mejores_delanterosR(pos+1,jugadores,goles_min,posicion)

    return candid_goleador

#Probador
#print(mejores_delanterosR(0,jugadores,20,posicion))

def mostrar_clubs(jugadores,posicion):

    """ tupla(tJugador) -> Nada.
    OBJ: Mostar clubes con candidatos al  mejor goleador.
    PRE: Nada. """

    candidatos = mejores_delanteros(jugadores,posicion,20)

    jugadores_vistos = []

    for jugador in jugadores:

        if(jugador in candidatos and jugador.equipo not in jugadores_vistos):

            jugadores_vistos.append(jugador.equipo)

            print(jugador.equipo,'-',candidatos.count(jugador.equipo))

#Probador
#mostrar_clubs(jugadores,posicion)

def cuantos_candidatos(jugadores,equipo):

    """ lista, tupla(tJugadores) -> int
    OBJ: Calcular cuantos delanteros de un equipo esta entre los candidatos."""

    candidatos = mejores_delanteros(jugadores,posicion,20)

    x = 0


        

    return candidato

#print(cuantos_candidatos(jugadores,'FCBarcelona'))
    




        

        

    

