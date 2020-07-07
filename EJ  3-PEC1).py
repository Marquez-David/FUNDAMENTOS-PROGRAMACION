#Ejercicio 3
def serie_numerica(limite):
    """int-->int
    OBJ: imprime una serie numerica hasta un limite que elija el usuario
    PRE: el numero limitedebe ser entero. """
    longuitud = 0
    a_siguiente = 1
    b_siguiente = 2
    while (longuitud != limite):
         x = (a_siguiente + b_siguiente)
         y = (a_siguiente + a_siguiente * b_siguiente)
         print(x , "/" , y)
         longuitud = longuitud + 1
         a_siguiente = x
         b_siguiente = y
try:
    serie_numerica(int(input("Limite de la serie:   ")))
except:
    print("El limite debe ser un entero")
