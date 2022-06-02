""" Modulo Vacunadores
    Funciones para el manejo de vacunas mensuales
    con matrices
    Oscar Franco-Bedoya
   Abril-2022 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================



def que_mes_es(numero):
    meses = {1:"Enero",2:"Febrero",3:"Marzo",
         4:"Abril",5:"Mayo",6:"Junio",
         7:"Julio",8:"Agosto",9:"Septiembre",
         10:"Octubre",11:"Noviembre",12:"Diciembre"}
    return meses[numero]

def leer_numero_empleados(empleados):
    num_empleados = len(empleados)
    print("El numero de empleados es:",num_empleados)
    return num_empleados

def leer_ventas_empleados_mes(empleados,mes):
    totalesEmpleados = []
    for empleado in empleados:
        total = [empleado[0],empleado[mes]]
        totalesEmpleados.append(total)
        print(empleado[0]," realizo ",empleado[mes]," vacunas en el mes ",que_mes_es(mes))

def total_ventas_por_vendedores(empleados):
    for empleado in empleados:
        # print(empleado)
        total = 0
        for e in empleado:
            if(isinstance(e,int)):
                total += e
        empleado.append(total)
    #print(empleados)
        
def ordenar_vendeores_por_ventas(empleados):
    total_ventas_por_vendedores(empleados)
    empleados.sort(key=lambda x:x[13], reverse= True)
    #print('El total de vacunas es el siguiente: \n')
    #for empleado in empleados:
        # print(empleado[0], "Realizo ",empleado[13]," vacunas en el año")

def calcular_cinco_vendedores(empleados):
    total_ventas_por_vendedores(empleados)
    print("Top 5 de mejores vacunadores")
    i = 0
    while(i<5):
        print(empleados[i][0]," realizo ", empleados[i][13])
        i+=1

def calcula_mes_mas_ventas(empleados):
    ventaMensual=[0,0,0,0,0,0,0,0,0,0,0,0]
    for empleado in empleados:
        i = 0
        while(i<12):
            # if(ventaMensual[i] == 0):
            ventaMensual[i] += empleado[i+1]
            # print("Existe")
            # else:
            # print("no existe")
            # ventaMensual.append(empleado[i+1])
            i+=1
    mes = 0
    ventaMes = 0
    for i in range(0,12):
        if ventaMensual[i] > ventaMes:
            mes = i+1
            ventaMes = ventaMensual[i]
        # print(ventaMes," en ", que_mes_es(mes))
        # print(mes)
                
    print("El mes con mas vacunaciones fue: ", que_mes_es(mes)," con ", ventaMes, " vacunas")


def greficar_ventas_por_mes(empleados):
    pass
