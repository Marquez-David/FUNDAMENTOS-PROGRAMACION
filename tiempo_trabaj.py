"""

***************************************************************
*    Nombre: Tiempo_Trabaj.py                                 *
*    Objetivo: Calcula el tiempo trabajado de un usuario.     *
***************************************************************

"""

def tiempo_trabaj(h_entr,m_entr,h_sal,m_sal):

    """ int, int, int, int --> Nada
    OBJ: Calcula en tiempo trabajo de un empleado.
    PRE: Los valoresintroducidos,deben ser enteros. """

    if(h_sal<h_entr):

        h_sal += 24

    horas = h_sal - h_entr

    if(m_sal < m_entr):

        horas -= 1

        minutos = 60 - m_entr + m_sal

    else:

        minutos = m_sal - m_entr

    print(horas,"horas", ":",minutos,"minutos",)

    if(horas > 8 and minutos>0):

        print("Error: Un empleado  no puede trabajar mas d 8 horas.")
        

    
try:
    
    tiempo_trabaj(int(input("Hora entrada: ")), int(input("Minuto entrada: ")), int(input("Hora salida: ")), int(input("Minuto salida: ")))

except ValueError:

    print("Debes introducir numeros enteros. ")
    
    
    
        
