#diccionarios a usar

Escuderias = {}
Conductores = {}
Circuitos = {}
Calendario = {}
Competencia = {}

#funciones para el modulo 1
def agregar_datosM1 ():
    global Escuderias
    IdEsc1 = int(input("Ingrese el numero del ID de la escuderia: "))
    Nombre1 = input("Ingrese el nombre de la escuderia: ")
    PaisBase1 = input("Ingrese el pais base de la escuderia: ")
    CampeonatoWin1 = int(input("Ingrese la cantidad de campeonatos ganados: "))
    PuntosCon1 = int(input("Ingrese los puntos del conductor 1: "))
    PuntosCon2 = int(input("Ingrese los puntos del conductor 2: "))
    PuntosEsc = int(PuntosCon1 + PuntosCon2)
    Escuderias[IdEsc1] = Nombre1, PaisBase1, CampeonatoWin1, PuntosEsc

def eliminar_Escuderia(id_Escuderia):
    global Escuderias
    del(Escuderias[id_Escuderia])
    print("Escuderia Eliminada")

def listar_Escuderias():
    global Escuderias
    for user1 in Escuderias:
        print(
    """
    IdEscuderia: {}
    Nombre: {}
    PaisBase: {}
    CampeonatosGanados: {}
    Puntos: {}
    """.format(user1, Escuderias[user1][0], Escuderias[user1][1], Escuderias[user1][2], Escuderias[user1][3]))

#funciones para el modulo 2
def agregar_datosM2 ():
    global Conductores
    IdCon = input("Ingrese el nombre o ID del conductor: ")
    IdEsc2 = int(input("Ingrese el Id de la escuderia: "))
    PaisCon = input("Ingrese el pais de origen del conductor: ")
    PuntosCon = int(input("Ingrese el Puntaje del conductor: "))
    Conductores[IdCon] = IdEsc2, PaisCon, PuntosCon

def eliminar_Conductores(id_Conductores):
    global Conductores
    del(Conductores[id_Conductores])
    print("Conductor Eliminado")

def listar_Conductores():
    global Conductores
    for user2 in Conductores:
        print(
    """
    Nombre: {}
    IdEscuderia: {}
    PaisOrigen: {}
    Puntos: {}
    """.format(user2, Conductores[user2][0], Conductores[user2][1], Conductores[user2][2]))

#funciones para el modulo 3
def agregar_datosM3():
    global Circuitos
    IdCir = input("Ingrese el nombre o Id del Circuito: ")
    PaisCir = input("Ingrese el pais del Circuito: ")
    Circuitos[IdCir] = PaisCir

def eliminar_Circuitos(Id_Circuitos):
    global Circuitos
    del(Circuitos[Id_Circuitos])
    print("Circuito Eliminado")

def listar_Circuitos():
    global Circuitos
    for user3 in Circuitos:
        print(
    """
    Circuito: {}
    Pais: {}
    """.format(user3, Conductores[user3][0]))

#funciones para el modulo 4
def agregar_datosM4():
    global Calendario
    IdCir = input("Ingrese el nombre o ID del circuito: ")
    print("Ingrese las fechas solicitadas con numeros")
    Año = int(input("Ingrese el año:"))
    DiaInicio = int(input("Ingrese la fecha del dia del inicio: "))
    DiaFinal = int(input("Ingrese la fecha del dia de finalizacion: "))
    mes = int(input("Ingrese el mes: "))
    Calendario[IdCir] = Año, DiaInicio, DiaFinal, mes

def eliminar_Calendarios(id_Calendario):
    global Calendario
    del(Calendario[id_Calendario])
    print("Fechas eliminadas")

def listar_Calendarios():
    global Calendario
    for user4 in Calendario:
        print(
    """
    Circuito: {}
    Año: {}
    DiaInicio: {}
    DiaFinal: {}
    Mes: {}
    """.format(user4, Calendario[user4][0], Calendario[user4][1], Calendario[user4][2], Calendario[user4][3], Calendario[user4][4]))

#funciones para el modulo 5

def agregar_datosM5():
    global Competencia
    IdCom = input("Ingrese el ID de la competencia: ")
    IdCon = input("Ingresa el nombre o ID del conductor: ")
    IdCir = input("Ingresa el nombre o ID del circuito: ")
    Año = input("Ingrese el año: ")
    Posicion = input("Ingrese la posicion: ")
    Tiempo = int(input("Ingrese la duracion de la competencia: "))
    MejorVuelta = input("Ingrese el tiempo de la mejor vuelta: ")
    Competencia[IdCom] = IdCon, IdCir, Año, Posicion, Tiempo, MejorVuelta

def eliminar_Competencias(Id_Competencia):
    global Competencia
    del(Competencia[Id_Competencia])
    print("Comptencia eliminada")

def listar_Competencias():
    global Competencia
    for user4 in Competencia:
        print(
    """
    IdCompetencia: {}
    IdConductor: {}
    IdCircuito: {}
    Año: {}
    Posicion: {}
    Tiempo: {}
    MejorVuelta: {}
    """.format(user4, Competencia[user4][0], Competencia[user4][1], Competencia[user4][2], Competencia[user4][3], Competencia[user4][4], Competencia[user4][5]))
#funciones para el modulo 6


while True:
    # interfaz para el uso de los modulos
    print(
        "---------------------------------",
        "Elija el Modulo a usar",
        "insertando el numero de modulo",
        "1.Modulo Escuderias",
        "2.Modulo Conductores",
        "3.Modulo Circuitos",
        "4.Modulo Calendarios",
        "5.Modulo Competencia",
        "6.Modulo Clasificacion",
        "7.Salir",
        "---------------------------------",
        sep='\n'
    )
    NumSeleccion = int(input("Selecciona el modulo a usar: "))

    if NumSeleccion == 1:
        while True:
            print(
            "---------------------------------",
            "Seleccione una funcion",
            "1. agregar datos",
            "2. Eliminar datos",
            "3. Ver datos",
            "4. Salir",
            "---------------------------------",
            sep='\n'
            )
            Func1 = int(input("Selecciona la funcion a usar: "))
            if Func1 == 1:
                agregar_datosM1()
            elif Func1 == 2:
                id_Escuderia = int(input("Ingrese el Id de la escuderia: "))
                eliminar_Escuderia(id_Escuderia)
            elif Func1 == 3:
                listar_Escuderias()
            elif Func1 == 4:
                    break

    if NumSeleccion == 2:
        while True:
            print(
            "---------------------------------",
            "Seleccione una funcion",
            "1. agregar datos",
            "2. Eliminar datos",
            "3. Ver datos",
            "4. Salir",
            "---------------------------------",
            sep='\n'
            )
            Func2 = int(input("Selecciona la funcion a usar: "))
            if Func2 == 1:
                agregar_datosM2()
            elif Func2 == 2:
                id_Conductores = int(input("Ingrese el nombre o ID del conductor: "))
                eliminar_Conductores(id_Conductores)
            elif Func2 == 3:
                listar_Conductores()
            elif Func2 == 4:
                    break

    if NumSeleccion == 3:
        while True:
            print(
            "---------------------------------",
            "Seleccione una funcion",
            "1. agregar datos",
            "2. Eliminar datos",
            "3. Ver datos",
            "4. Salir",
            "---------------------------------",
            sep='\n'
            )
            Func3 = int(input("Selecciona la funcion a usar: "))
            if Func3 == 1:
                agregar_datosM3()
            elif Func3 == 2:
                Id_Circuitos = int(input("Ingrese el nombre o ID del Circuito: "))
                eliminar_Circuitos(Id_Circuitos)
            elif Func3 == 3:
                listar_Circuitos()
            elif Func3 == 4:
                    break

    if NumSeleccion == 4:
        while True:
            print(
            "---------------------------------",
            "Seleccione una funcion",
            "1. agregar datos",
            "2. Eliminar datos",
            "3. Ver datos",
            "4. Salir",
            "---------------------------------",
            sep='\n'
            )
            Func4 = int(input("Selecciona la funcion a usar: "))
            if Func4 == 1:
                agregar_datosM4()
            elif Func4 == 2:
                id_Calendario = int(input("Ingrese el nombre o ID del Calendario: "))
                eliminar_Calendarios(id_Calendario)
            elif Func4 == 3:
                listar_Calendarios()
            elif Func4 == 4:
                    break

    if NumSeleccion == 5:
        while True:
            print(
            "---------------------------------",
            "Seleccione una funcion",
            "1. agregar datos",
            "2. Eliminar datos",
            "3. Ver datos",
            "4. Salir",
            "---------------------------------",
            sep='\n'
            )
            Func5 = int(input("Selecciona la funcion a usar: "))
            if Func5 == 1:
                agregar_datosM5()
            elif Func5 == 2:
                Id_Competencia = int(input("Ingrese el nombre o ID de la competencia: "))
                eliminar_Competencias(Id_Competencia)
            elif Func5 == 3:
                listar_Competencias()
            elif Func5 == 4:
                    break

    elif NumSeleccion == 7:
        break
    else:
        print("Selecciona un modulo")
