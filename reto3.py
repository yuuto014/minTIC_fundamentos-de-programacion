#Imprimimos un mensaje con las instrucciones iniciales para el usuario
def informacion():
    print("******************************************")
    print("Bienvenido jugador de WorldCraft ASCII")
    print("Para ingresar se necesita una cadena de 10 caracteres que debe cumplir los siguientes requerimientos:")
    print("-No debe contener numeros")
    print("-El primer y ultimo caracter tienen que ser diferentes")
    print("-En la posicion 6 debe tener un @")
    print("-Debe contener el siguiente caracter '+'")
    print("-Debe contener alguno de los siguientes caracteres '?','=','&'")
    print("-NO tener mas de 3 letras 'k'")
    print("******************************************")
#Funcion para verificar que el CDIA sea correcto
def validar_CDIA(cdia):
#se valida si el string tiene 10 caracteres con el metodo len
    if len(cdia) != 10:
        #print("El CDIA  no tiene 10 caracteres")
        print("CDIA inválido")
        return 0
#Se valida si algun caracter del string tiene un numero con el metodo  isdigit
    elif any(chr.isdigit() for chr in cdia):
        #print("El CDIA tiene numeros")
        print("CDIA inválido")
        return 0
#Se valida si en la posicion 6 hay un @
    elif cdia[6] != "@":
        #print("El CDIA no tiene el @ en la posicion correcta")
        print("CDIA inválido")
        return 0
#Se valida que tanto el ultimo caracter como el primero sean diferentes
    elif cdia[0] == cdia[9]:
        #print("El primer caracter y el ultimo son iguales")
        print("CDIA inválido")
        return 0
#Se valida que el caracter + se encuentre en el CDIA
    elif "+" not in cdia:
        #print("No se encuentra el caracter '+' en el CDIA")
        print("CDIA inválido")
        return 0
#Se valida que se encuentre al menos alguno de los caracteres
    elif "?" not in cdia and "=" not in cdia and "&" not in cdia:
        #print("El CDIA debe tener al menos uno de estos caracteres ‘?’,’=’,’&’")
        print("CDIA inválido")
        return 0
#se valida que no tenga mas de 3 letras k 
    elif cdia.count("K") > 3 :
        print("Tiene mas de 3 letras k")
        print("CDIA inválido")
        return 0
#Al pasar todos los filtros, se determina que esta bien el CDIA
    else:
#Hace falta el metodo para buscar el CDIA en la lista de otros usuarios
        #if asc.buscar_cdia(dia):
        print("CDIA leído y correcto")
        return 1
        #else: 
        #  return 0
    print("******************************************")
#Funcion para determinar la edad
def Edad():
    nacimiento = input("Ingrese su edad en el siguiente formato DD/MM/AAAA: ")
    year= int(nacimiento[6:10])
    month = int(nacimiento[3:5])
    day = int(nacimiento[0:2])

    if month <= 5 and day <= 15:
        return 2021 + 1 - year
    else:
        return 2021 - year
#funcion para validar el alias del usuario
def validar_alias(alias):
    if " " in alias:
        print("El alias ingresado tiene espacios")
        return False
    elif len(alias) < 5:
        print("El alias ingresado tiene menos de 5 caracteres")
        return False
    else:
        return True
#Funcion para determinar si el jugardor ha jugado antes
def validarSiHaJugado():
    jugardor = input("¿Ya has jugado WorldCraft ASCII? (Si, No)").upper() 
    if jugardor =="SI":
        return True
    else :
        return False
#Funcion para preguntar de el nivel del jugador
def nivelPasado():
    nivelAnterior = int(input("Digite al ultimo nivel que llego: "))
    if 1<nivelAnterior<=100:
        return nivelAnterior
    else:
        print("Nivel no valido, se le asigno temporalmente el nivel 0")
        return 0
#Funcion para asignarle el nuevo nivel al usuario
def nuevoNivel(edad, nivelAntiguo):
    if edad < 16 and nivelAntiguo == 0:
        return 2
    elif edad < 16 and nivelAntiguo >1:
        return nivelAntiguo
    elif edad >= 16 and nivelAntiguo==0:
        return 1
    elif edad >= 16 and nivelAntiguo >= 98:
        return 100
    else:
        return nivelAntiguo + 2
#Funcion para asignar el mundo
def asignacionMundo(edad, nivel,jugador):
    if 12<=edad<=20 and not jugador:
        return 1
    elif 12<=edad<=20 and jugador and nivel<50:
        return 2
    elif 12<=edad<=20 and jugador and nivel>=50:
        return 3
    elif edad>20 and not jugador:
        return 4
    elif edad>20 and jugador and nivel<50:
        return 5
    elif edad>20 and jugador and nivel>=50:
        return 6
#Funcion que muestra los datos ingresados
def bienvenido(cdia,alias,nivel,mundo):
    print("******************************************")
    print("Bienvenid@ ",alias, " al Mundo",mundo)
    print("tu nivel es: ", nivel)
    print("Tu codigo de identificacion ASCII es: ",cdia)
    print("******************************************")
#Empezamos a mostrar informacion
informacion()
#Se recibe el CDIA
cdia="asgdjk@=+d".upper()
#cdia = input("Ingrese su codigo ASCII: ").upper()#asgdjk@=+d
#Se valida que el codigo ingresado sea correcto
valido = validar_CDIA(cdia)
#si el codigo es valido procedemos a verificar la edad y si es mayor de 12 a que conteste las preguntas
if valido:
    #edad = Edad()
    edad = 21;
    if edad >= 12:
        #alias = input("Escriba un alias de al menos 5 caracteres y sin espacios:")
        alias = "pedroo"
        aliasValido = validar_alias(alias)
        if aliasValido:
            esJugador = validarSiHaJugado()
            if esJugador:
                nivelAntiguo = nivelPasado()
            else :
                nivelAntiguo = 0 
            nivel = nuevoNivel(edad, nivelAntiguo)
            mundo = asignacionMundo(edad,nivelAntiguo,esJugador)
            bienvenido(cdia,alias,nivel,mundo)
        else:
            print("Su alias no es valido")
    else :
        print("No cumple la edad minima para jugar")
  