#Propuesta solucion PEC1

# Constantes.

FLOTA = ('0410FJB','2222HIJ','MU-1388','8888XYZ','9999XYK')

h_alk=(10.0, 72.0, 30.0, 32.5, 28.5)

mant=(75.42, 17.71, 22.42, 23.63, 19.83)

tipo=(1, 2, 3, 3, 2)

tipos_coche=('furgo', '4p', '5p')

fianzas=(150.00, 100.00, 50.00, 50.00, 100.00)

precio_h=(22.00, 8.30, 10.50, 10.50, 8.30)

costes=((22.00, 8.30, 10.5), (150, 100, 50))

ingresos_coche=(220.00, 597.60, 315.00, 341.25, 236.55)


#Apartado b)

def ingreso_coche(matricula, flota, h_alk, precio_h):
    """str --> float
       OBJ: Dar coste de cada coche
       Pre:        """
    
    tupla_costes=()
    
    if matricula == flota[0]:
        
        tupla_costes=(flota[0],(costes[0][0])*h_alk[0])
        
    elif matricula == flota[1]:
        
        tupla_costes=(flota[0],(costes[0][1])*h_alk[1])
        
    elif matricula == flota[2]:
        
        tupla_costes=(flota[0],(costes[0][2])*h_alk[2])
        
    elif matricula == flota[3]:
        
        tupla_costes=(flota[0],(costes[0][2])*h_alk[3])
        
    else:
        
        tupla_costes=(flota[0],(costes[0][1])*h_alk[4])
        
    return tupla_costes

print(ingreso_coche('0410FJB', flota, h_alk, precio_h), '0410FJB, 220.0')
print(ingreso_coche('2222HIJ', flota, h_alk, precio_h), '2222HIJ, 597.6')
print(ingreso_coche('MU-1388', flota, h_alk, precio_h), 'MU-1388, 315.0')
print(ingreso_coche('8888XYZ', flota, h_alk, precio_h), '8888XYZ, 341.25')
print(ingreso_coche('9999XYK', flota, h_alk, precio_h), '9999XYK, 236.55')

 

#Apartado c)

def ingresos_totales_mes(h_alk, precio_h):
    """ tupla, tupla ---> float
         OBJ: Dar ingresos totales del mes"""
    cont=0
    for i in range(0,len(h_alk)):
        cont+= h_alk[i]*precio_h[i]
    return round(cont,5)

print(ingresos_totales_mes(h_alk, precio_h), '1710.4')


#Apartado d)

def pos_ingreso_mensual_mayor(ingresos_coche):
    """ tupla ---> int
        OBJ: Indicar posicion del coche de mayores ingresos
        Pre:   """
    pos_mayor=0
    for pos in range(1,len(ingresos_coche)):
        if ingresos_coche[pos]>ingresos_coche[pos_mayor]:
            pos_mayor=pos
    return pos_mayor+1

print(pos_ingreso_mensual_mayor(ingresos_coche),'2')


#Apartado e)

def tipo_coche(matricula, flota, tipo, tipos_coche):     #Se utiliza la matricula como referencia del coche
    """ str, tupla(int), tupla(str) ---> int, str
        OBJ: Dar tipo de coche
        Pre:  """    if matricula == flota[0]:
        ntipo= 1
        tipo='furgo'
    elif matricula == flota[1] or matricula == flota[4]:
        ntipo= 2
        tipo='4p'
    else:
        ntipo= 3
        tipo='5p'
    return ntipo, tipo

print(tipo_coche('0410FJB', flota, tipo, tipos_coche), '1, furgo')
print(tipo_coche('2222HIJ', flota, tipo, tipos_coche), '2, 4p')
print(tipo_coche('MU-1388', flota, tipo, tipos_coche), '3, 5p')
print(tipo_coche('8888XYZ', flota, tipo, tipos_coche), '3, 5p')
print(tipo_coche('9999XYK', flota, tipo, tipos_coche), '2, 4p')        

 

#Apartado f)

from libInterfaz import realPedido
horas_alk_1=realPedido(0, 35, 'Dime las horas alquiladas del vehiculo "0410FJB":')
horas_alk_2=realPedido(0, 35, 'Dime las horas alquiladas del vehiculo "2222HIJ":')
horas_alk_3=realPedido(0, 35, 'Dime las horas alquiladas del vehiculo "MU-1388":')
horas_alk_4=realPedido(0, 35, 'Dime las horas alquiladas del vehiculo "8888XYZ":')
horas_alk_5=realPedido(0, 35, 'Dime las horas alquiladas del vehiculo "9999XYK":')
mant_1=realPedido(0, 2000, 'Dime el coste de mantenimiento del vehiculo "0410FJB":')
mant_2=realPedido(0, 2000, 'Dime el coste de mantenimiento del vehiculo "2222HIJ":')
mant_3=realPedido(0, 2000, 'Dime el coste de mantenimiento del vehiculo "MU-1388":')
mant_4=realPedido(0, 2000, 'Dime el coste de mantenimiento del vehiculo "8888XYZ":')
mant_5=realPedido(0, 2000, 'Dime el coste de mantenimiento del vehiculo "9999XYK":')

print(sep='\n')

print('Matricula', 'tipo', 'alq/h', 'h', 'mant', 'fianza', sep='\t')
print(flota[0], '   ', tipo[0], precio_h[0], horas_alk_1, mant_1, costes[1][0], sep='\t')
print(flota[1], '   ', tipo[1], precio_h[1], horas_alk_2, mant_2, costes[1][1], sep='\t')
print(flota[2], '   ', tipo[2], precio_h[2], horas_alk_3, mant_3, costes[1][2], sep='\t')
print(flota[3], '   ', tipo[3], precio_h[3], horas_alk_4, mant_4, costes[1][2], sep='\t')
print(flota[4], '   ', tipo[4], precio_h[4], horas_alk_5, mant_5, costes[1][1],) sep='\t'
