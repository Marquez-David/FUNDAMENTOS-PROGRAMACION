#Ejercicio 2 extra
print("Opcion 0: no se realiza ninguna operacion y finaliza el programa")
print("Opcion 1: realiza una suma entre dos numeros")
print("Opcion 2: Realiza una resta entre dos numeros")
print("Opcion 3:Realiza una multiplicacion entre dos numeros")
print("Opcion 4:Realiza una division entre dos numeros")
def calculadora(a,b,x):
    """float-->float
    OBJ: muestra por pantalla una serie de opciones para que el usuario elija"""
    while (x >= 0 and x <=4):
        if ( x == 1):
           suma = a + b
           print("La suma de tus numeros es: " , suma)
        elif ( x == 2):
            resta = a - b
            print ("La resta entre los valores es: " , resta)
        elif ( x == 3):
            multiplicacion = a*b
            print("El resultado de la multiplicacion es: " , multiplicacion )
        elif ( x == 4):
            division = a/b
            print("El resultado de la division es: " , division)
        elif ( x == 0):
            break
        x = int(input("Elije una opcion: "))
    else: 
        print("Debes introducir valores entre 0 y 4")
try:
    calculadora(float(input("Introduce elprimer numero: ")) , float(input("Introduce el segundo numero: ")) , int(input("Elije una opcion: ")))
except:
    print("Error: el valor introducido no es correcto")
