""" Modulo Vacunadores
    Funciones para el manejo de vacunas mensuales
    con matrices
    Oscar Franco-Bedoya
   Abril-2022 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
# meses = {1:"Enero",2:"Febrero",3:"Marzo",
#          4:"Abril",5:"Mayo",6:"Junio",
#          7:"Julio",8:"Agosto",9:"Septiembre",
#          10:"Octubre",11:"Noviembre",12:"Diciembre"}

def leer_numero_empleados(empleados):
    num_empleados = len(empleados)
    print(num_empleados)
    return num_empleados

def leer_ventas_empleados_mes(empleados,mes):
    totalesEmpleados = []
    for empleado in empleados:
        total = [empleado[0],empleado[mes]]
        totalesEmpleados.append(total)
        print(empleado[0]," realizo ",empleado[mes]," vacunas en el mes ",mes)

def total_ventas_por_vendedores(empleados):
    for empleado in empleados:
        # print(empleado)
        total = 0
        for e in empleado:
            if(isinstance(e,int)):
                total += e
        empleado.append(total)
    print(empleados)
        

def ordenar_vendeores_por_ventas(empleados):
    #TODO Comentar código
    #TODO Implementar la función
    return "No implementada aún"

def calcular_cinco_vendedores():
    #TODO Comentar código
    #TODO Implementar la función
    return "No implementada aún"

def calcula_mes_mas_ventas():
    #TODO Comentar código
    #TODO Implementar la función
    return "No implementada aún"

def greficar_ventas_por_mes():
    #TODO Comentar código
    #TODO Implementar la función
    return "No implementada aún"