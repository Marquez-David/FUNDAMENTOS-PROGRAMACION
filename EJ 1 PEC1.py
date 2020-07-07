def imagen_numeros(a,b):
    """ int--> int 
    OBJ: el programa pide el usuariodos numeros y retorna si son imagen uno del otro o no.
    PRE: los  numeros deben ser enteros. """
    unidad_a = a % 10
    decena_a = (a//10) % 10
    centena_a = (a//100) % 10
    unidad_b = b % 10
    decena_b = (b//10) % 10
    centena_b = (b//100) % 10
    if (unidad_a==centena_b):
        print("El primer numero coincide")
    if (decena_a==decena_b):
        print("El segundo numero coincide")
    if (centena_a==unidad_b):
        print("El numero a es la imagen del numero b ")
    else: 
        print("Los numeros a y b no son imagen")
try:
    imagen_numeros(int(input("Introduce un numero: ")) , int(input("Introduce un segundo numero: ")))
except:
    print("Los numeros deben ser enteros")
