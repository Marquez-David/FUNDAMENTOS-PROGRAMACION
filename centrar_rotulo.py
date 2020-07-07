"""

********************************************************
*          Nombre: centrar_rotulo.py                   *
*          Objetivo: Centra el rotulo en la pantalla.  *
********************************************************

"""

def centrar_rotulo(txt,simb):

    """ String, String --> Nada
    OBJ: Centrar en la pantalla un texto introducido. """

    tam_pantalla = 80

    tam_txt = len(txt)

    esp_blanco = (tam_pantalla - tam_txt)//2

    print(" "*esp_blanco, txt, "\n"," "*(esp_blanco -1), simb*tam_txt )

#centrar_rotulo(txt, str(input("Simbolo de subrayado: ")))                                                                                                                                                       
