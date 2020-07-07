"""

    Nombre: Cambio Formato Hora.
    OBJ: Cambia el formato de una fecha introducida por teclado.
    PRE: 0 < Dias < 24 , 0 < Horas < 60.

"""

def cambio_formato_hora(hora,minutos):

        if(hora > 12):

            hora -= 12

        print("Hora: ", hora, "Minutos: ", minutos)

cambio_formato_hora(int(input("Hora: ")), int(input("Minutos:")))

