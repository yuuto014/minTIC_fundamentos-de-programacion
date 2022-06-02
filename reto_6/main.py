""" Programa ventas 
    Programa para el manejo de vacunados por mes
    incorpora al modulo vacunas.py
    """

#---------------- Zona librerias------------
import vacunas as vt



#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

#empleados
def separador():
  print("************************************************")
empleados = [
  ["Andres",10,3,6,23,53,1,0,53,1,0,3,12],
  ["Pedro",5,23,1,7,3,0,21,3,7,12,8,2],
  ["Sandra",5,2,10,17,7,0,0,0,23,2,2,0],
  ["Roberto",0,0,0,0,3,6,4,7,2,10,20,1],
  ["Patricia",5,2,7,3,78,3,8,12,5,8,3,12],
  ["Claudia",34,1,3,6,7,23,7,29,4,0,0,0]
]


numEmpleados = vt.leer_numero_empleados(empleados);
separador()
mes = int(input("Que mes desea ver (1-12): "))
vt.leer_ventas_empleados_mes(empleados,mes)
separador()

vt.calcular_cinco_vendedores(empleados)
separador()

vt.calcula_mes_mas_ventas(empleados)
separador()

vt.graficar_ventas_por_mes(empleados)






"""
empleados = [
  ["Andres"],
  ["Pedro"],
  ["Sandra"],
  ["Roberto"],
  ["Patricia"],
  ["Claudia"]
]"""

#lista de empleados llena
"""
empleados = {
    "Nombre": ["Andres","pedro","Sandra","Roberto","Patricia","Claudia"],
    "Enero":[10,5,5,0,5,34],
    "Febrero":[3,5,62,5,2,6],
    "Marzo":[2,2,5,7,1,0],
    "Abril":[0,0,3,7,3,2],
    "Mayo":[2,8,4,0,12,7],
    "Junio":[0,0,6,3,7,21],
    "Julio":[21,6,8,1,0,0],
    "Agosto":[5,2,7,0,1,5],
    "Septiembre":[2,7,2,8,3,9],
    "Octubre":[8,2,9,3,0,13],
    "Noviembre":[11,9,4,28,9,45],
    "Diciembre":[1,6,3,7,2,9],
    "Total":[0,0,0,0,0,0],
}
"""