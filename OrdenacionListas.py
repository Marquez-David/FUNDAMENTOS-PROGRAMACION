def distrubucion_de_datos(ListaDatos):
    """Lista,-->lista,lista
    OBJ: apartir de una lista de datos, crea dos listas nuevas 
         una ordenada crecientemente y otra decrecientemente.
    PRE: lalista d datos debe ser entera. """
    ListaAscendente = []
    ListaDescendente = []
    ListaAscendente = sorted(ListaDatos)
    ListaDescendente = sorted(ListaDatos)
    ListaDescendente.reverse()
    print("La lista ascendente es: " , ListaAscendente)
    print("La lista descendente es: " , ListaDescendente)
#Programa probador
ListaDatos = [2,4,12,45,23,7,22,56,99,21,3,69,98,76,32,13,14,19,84,61]
ListaAscendente = distrubucion_de_datos(ListaDatos) 
 
