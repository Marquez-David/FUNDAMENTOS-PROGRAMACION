"""
    Nombre: Cuadrado de asteriscos.
    OBJ: Crea un cuadrado de asteristos con lado determinado por el  usuario.
    PRE: El numero introducido debe ser entero positivo.

"""

n = int(input("Lado: "))

print("*" * n)

for i in range(n-2):

    if ( n>=5): print("*" ," "*(n-4), "*")

    elif ( n<5 and n>0): print("*" ," "*(n-5), "*")

print("*" * n)
