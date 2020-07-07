"""

    Nombre: Solicitante Valido.
    OBJ: Determina si una ersonaes valida para un prestamo.

"""

def anios_trabajados(anios):

    """ int --> bool
    OBJ: Determinar si ha trabajo mas de 5 anios.
    PRE: El valor introducido debe ser un entero > 0.
    """

    if(anios >= 5):

        valido = True

    else:

        valido = False

    return valido

def comparacion_sueldo_vivienda(sueldo,precio_vivienda):
    """ float , float --> bool
    OBJ: Determinar si el sueldo es el 20% el precio de la vivienda.
    PRE: Los avalores introducidos deben ser > 0.
    """

    if ( sueldo * 20/100 >= precio_vivienda):

        valido = True

    else:

        valido = False

    return valido

def comparacion_ingresos_compra(ingresos_anuales,precio_compra):

    """ float, float --> bool
    OBJ: Compara los ingresos anuales y el recio de la compra.
    PRE: Los valores introducidos deben ser > 0.
    """

    if( ingresos_anuales * 40/100 >= precio_compra):

        valido = True

    else:

        valido = False

    return valido

def comparacion_creditos_sueldo(otros_creditos,sueldo_anual):

    """ float, float --> bool
    OBJ: Comparar los creditos y el sueldo anual.
    PRE: Los valores  introducidos deben ser > 0.
    """

    if( otros_creditos < sueldo_anual* 20/100):

        valido = True

    else:


        valido = False

    return valido

def validar_solicitante():

    """ Nada --> Bool
    OBJ: Determina si un solicitante es valido para un credito.
    """

    if(Valido1 and Valido2 and Valido3 and Valido4 ):

        valido = True

        print("Solicitante valido")

    else:

        valido = False

        print("Solicitante no valido ")

    return valido


Valido1 = comparacion_creditos_sueldo(float(input("Creditos: ")), float(input("Sueldo anual: ")))
Valido2 = anios_trabajados(int(input("Introduce ls anios trabajados: ")))
Valido3 = comparacion_sueldo_vivienda(float(input("Sueldo: ")), float(input("Precio vivienda: ")))
Valido4 = comparacion_ingresos_compra(float(input("Ingresos anuales: ")), float(input("Precio Compra: ")))
validar_solicitante()

