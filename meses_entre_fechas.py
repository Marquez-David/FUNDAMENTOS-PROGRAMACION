"""

    Nombre: Meses entre fechas.
    OBJ: Calcula  los meses que hay entre dos fechas dadas.
    PRE: Los datos introducidos debe ser enteros > 0 y < 30.

"""

def entre_fechas(d1,m1,d2,m2):

    """ int , int ,int ,int  --> int
    OBJ: Calcula los meses entre dos fechas.
    PRE: PRE: Los datos introducidos debe ser enteros > 0 y < 30.
    """

    dias = 0

    dias += 30 - d1

    dias += 30 - d2

    meses =  m2 -m1 + dias // 30

    print("Meses: ", meses)

entre_fechas(int(input("Dia 1: ")), int(input("Mes 1: ")),
             int(input("Dia 2: ")), int(input("Mes 2: ")))
