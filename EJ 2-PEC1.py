#Ejercicio 2
def serie_numeros(nums):
    """int-->int
    OBJ: a partir de una serie determinada de numeros determina si el numero en concreto se situa en esa lista, tambien determina la posicion en la lista
    demas del numero mas cercano junto con su posicion. 
    PRE: los numeros deben ser enteros. """
    premiado = 13
    CENTINELA = -9999
    posicion = 0
    num_anterior = 12
    posicion_anterior = 0
    while (nums != CENTINELA):
        if ( nums == 13 ):
            print("El numero premiado es 13")
            print("El numero premiado se situa enla posicion: " , posicion)
        if (nums + 1 == premiado):
            print("El numero anterior se situa en la posicion: " , posicion_anterior)
        posicion = posicion + 1
        posicion_anterior = posicion_anterior + 1
        nums = int(input("Introduce un valor para la serie(-9999 para terminar): "))
        if ( nums != 13):
            print("El numero premiado aparece en la posicion - 1
try:
    serie_numeros(int(input("Introduce un valor para la serie(-9999 para terminar): ")))
except:
    print("El valor introducido debe ser un entero")
