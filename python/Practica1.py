import random

while True:
    # interfaz para el uso de los Anexos
    print(
        "---------------------------------",
        "Elija el anexo a usar",
        "insertando el numero de anexo",
        "1.Anexo 1",
        "2.Anexo 2",
        "3.Salir",
        "---------------------------------",
        sep='\n'
    )
    NumPro0 = int(input("Anexo a usar: "))  # Se pide el anexo a usar
    if NumPro0 == 1:
        while True:
            # Interfaz del anexo 1
            print(
                "---------------------------------",
                "Elija la funcion que desea usar",
                "insertando el numero de programa",
                "1.Usuario ¿Mayor o menor de edad?",
                "2.La contraseña es correcta ",
                "3.Numero Mayor",
                "4.De 3 numeros ¿Cual es el Mayor?",
                "5.¿El estudiante aprobó?",
                "6.¿Quieres saber cual es tu IMC",
                "7.Azar",
                "0.Salir",
                "---------------------------------",
                sep='\n'
            )
            NumPro1 = int(input("Funcion a usar: "))  # Se pide la funcion a usar

            if NumPro1 == 1:
                # Programa que dice si el usuario es mayor o no de edad si su edad es mayor o igual a 18
                Edad = int(input("Ingrese la edad en numeros: "))
                if Edad >= 18:
                    print("El usuario es mayor de edad")
                else:
                    print("El usuario es menor de edad")

            elif NumPro1 == 2:
                # Programa inserta la contraseña correcta
                Password = "Info2021"
                c = 0
                # Se repite hasta que se inserte la contraseña correcta o se intente mas de 3 veces
                while True:
                    c += 1
                    Cont = str(input("Ingrese la contraseña: "))
                    if Cont != Password:
                        print("contraseña incorrecta, intentelo de nuevo")
                    elif c == 3:
                        print("Lo has intentado muchas veces, vuelve a intentarlo en un rato")
                        break
                    else:
                        print("contraseña correcta puede continuar")
                        break

            elif NumPro1 == 3:
                # De 2 numeros se averigua cual es el mayor
                N1 = int(input("Inserte el primer numero: "))
                N2 = int(input("Inserte el segundos numero: "))
                if N1 > N2:
                    print("El numero 1 es el mayor: ", N1)
                    print("El numero 2 es el menor: ", N2)
                else:
                    print("El numero 2 es el mayor: ", N2)
                    print("El numero 1 es el menor: ", N1)

            elif NumPro1 == 4:
                # De 3 numeros se averigua cual es el mayor
                N1 = int(input("Inserte el primer numero: "))
                N2 = int(input("Inserte el segundos numero: "))
                N3 = int(input("Inserte el tercer numero:"))
                if N1 > N2:
                    if N1 > N3:
                        print("el numero mayor es: ", N1)
                else:
                    if N2 > N3:
                        print("el numero mayor es: ", N2)
                    else:
                        print("el numero mayor es: ", N3)
                print("los numeros eran: ", N1, N2, N3)

            elif NumPro1 == 5:
                # Saber si el estudiante paso sabiendo el promedio de la nota de sus 3 periodos
                Nota1 = int(input("Ingrese su primera nota: "))
                Nota2 = int(input("Ingrese su segunda nota: "))
                Nota3 = int(input("Ingrese su tercera nota: "))
                Promedio = (Nota1 + Nota2 + Nota3) / 3
                if Promedio >= 70:
                    print("Aprobado, el promedio es de: ", Promedio)
                else:
                    print("Reprobado, el promedio es de: ", Promedio)

            elif NumPro1 == 6:
                # Sacar el Indice de Masa Corporal, para saber si esta en un estado normal, de obesidad o de desnutricion
                Peso = int(input("Ingrese su Peso en kilogramos: "))
                Alt = float(input("Ingrese su altura en centimetros:  "))
                IMC = Peso / ((Alt / 100) * (Alt / 100))
                if IMC <= 29:
                    if IMC >= 19:
                        print("Su IMC es de: ", IMC, " Usted esta en un IMC normal")
                    else:
                        if IMC <= 19:
                            print("Su IMC es de: ", IMC, " Usted sufre de desnutrición")
                else:
                    print("Su IMC es de: ", IMC, " Usted sufre de obesidad")

            elif NumPro1 == 7:
                # Dado si los 2 numeros son iguales ganas si no pierdes
                Nu1 = random.randrange(1, 6)
                Nu2 = random.randrange(1, 6)
                if Nu1 == Nu2:
                    print("Ganaste los numeros eran: ", Nu1, " y ", Nu2)
                else:
                    print("Perdiste los numeros eran: ", Nu1, " y ", Nu2)

            elif NumPro1 == 0:
                # Se sale del anexo 1 y retrocede a la opcion para elegir el anexo a usar
                print("Saliendo, hasta pronto gracias por venir ˄˄")
                break
            else:
                print('No has seleccionado una opcion disponible, por favor seleccione una de las opciones disponibles')

    elif NumPro0 == 2:
        while True:
            # Interfaz para el anexo 2
            print(
                "---------------------------------",
                "Elija la funcion que desea usar",
                "insertando el numero de programa",
                "1.Repetición de nombres",
                "2.Suma X numeros",
                "3.Recuerdas la contraseña?",
                "4.Estudiante y su numero random",
                "5.Juego de verdadero o falso",
                "0.Salir",
                "---------------------------------",
                sep='\n'
            )
            NumPro2 = int(input("Funcion a usar: "))  # Se pide la funcion a usar
            if NumPro2 == 1:
                # Repite un nombre X cantidad de veces
                Nombre = str(input("Ingrese el nombre: "))
                Cant = int(input("Ingrese la cantidad de veces que quiere que se repita: "))
                c = 0
                while c != Cant:
                    c += 1
                    print(Nombre)

            if NumPro2 == 2:
                # Se pide un numero, después de piden la X cantidad de numeros pedidos para después sumarlos
                Numero = int(input("Ingrese la cantidad de numeros que desea usar: "))
                Suma = 0
                while Numero > 0:
                    N = int(input("Ingrese un numero: "))
                    Suma += N
                    Numero -= 1
                print("La suma de todos los numeros es de: ", Suma)

            if NumPro2 == 3:
                # Se tiene una contraseña secreta y el usuario tiene que insertarla
                Password2 = "CTP2021"
                c = 0
                while c != 3:
                    c += 1
                    IntPass = str(input("Ingrese la contraseña: "))
                    if IntPass == Password2:
                        print("Contraseña correcta, puede continuar: ")
                        break
                    else:
                        if c == 1:
                            print("Error, te quedan 2 intentos, vuelve a intentarlo")
                        if c == 2:
                            print("Error, te queda 1 intento")
                        if c == 3:
                            print("Acceso denegado, vuelve a intentarlo")

            if NumPro2 == 4:
                # Se inserta la cantidad de estudiantes, despues se piden los nombres y se les asigna un numero random
                CantEstudiantes = int(input("Ingrese la cantidad de estudiantes: "))
                c = 0
                while c != CantEstudiantes:
                    c += 1
                    Estudiante = str(input("Ingrese el nombre del estudiante: "))
                    NumeroRandom = random.randrange(0, CantEstudiantes)
                    print("El estudiante es: ", Estudiante, " y su numero aleatorio es: ", NumeroRandom)

            if NumPro2 == 5:
                Verdadero = "V"
                Falso = "F"
                Puntaje = 0
                print("Responda las preguntas con las letras V para verdadero y F para falso, en MAYUSCULAS ")

                Pregunta1 = str(input("¿Python es un lenguaje interpretado?: "))  # True
                # Se verifica si la respuesta esta correcta y se le asigna el puntaje
                if Pregunta1 == Verdadero:
                    Puntaje += 1
                    print("Felicidades +1 punto, tu puntaje por el momento es de: ", Puntaje, " Puntos")
                else:
                    print("Que mal, Era verdadera, tu puntaje por el momento es de:", Puntaje, " Puntos")

                Pregunta2 = str(input("¿Alan Turing participo en el desarrollo de python?: "))  # False
                # Se verifica si la respuesta esta correcta y se le asigna el puntaje
                if Pregunta2 == Falso:
                    Puntaje += 1
                    print("Felicidades +1 punto, tu puntaje por el momento es de: ", Puntaje, " Puntos")
                else:
                    print("Que mal, Era falsa, tu puntaje por el momento es de:", Puntaje, " Puntos")

                Pregunta3 = str(
                    input("¿El nombre de 'Python' proviene en honor a la serpiente con el mismo nombre?: "))  # False
                # Se verifica si la respuesta esta correcta y se le asigna el puntaje
                if Pregunta3 == Falso:
                    Puntaje += 1
                    print("Felicidades +1 punto, tu puntaje por el momento es de: ", Puntaje, " Puntos")
                else:
                    print("Que mal, Era Falsa, tu puntaje por el momento es de: ", Puntaje, " Puntos")

                Pregunta4 = str(input(
                    "¿Se puede usar funciones de otros archivos .py mientras esten en la misma carpeta?: "))  # True
                # Se verifica si la respuesta esta correcta y se le asigna el puntaje
                if Pregunta4 == Verdadero:
                    Puntaje += 1
                    print("Felicidades +1 punto, tu puntaje por el momento es de: ", Puntaje, " Puntos")
                else:
                    print("Que mal, Era verdadera, tu puntaje por el momento es de: ", Puntaje, " Puntos")

                Pregunta5 = str(
                    input("¿El siguiente fracmento de código esta correcto?, 'from pandas import *', V o F: "))  # True
                # Se verifica si la respuesta esta correcta y se le asigna el puntaje
                if Pregunta5 == Verdadero:
                    Puntaje += 1
                    print("Felicidades +1 punto, tu puntaje por el momento es de: ", Puntaje, " Puntos")
                else:
                    print("Que mal, Era verdadera, tu puntaje por el momento es de:", Puntaje, " Puntos")

                Pregunta6 = str(input("¿Python es un lenguaje de multiparadigma?: "))  # True
                # Se verifica si la respuesta esta correcta y se le asigna el puntaje
                if Pregunta6 == Verdadero:
                    Puntaje += 1
                    print("Felicidades +1 punto, tu puntaje por el momento es de: ", Puntaje, " Puntos")
                else:
                    print("Que mal, Era verdadera, tu puntaje por el momento es de: ", Puntaje, " Puntos")

                Pregunta7 = str(
                    input("¿La forma correcta para declarar una funcion es: def Nombre(Datos): Funcion?: "))  # True
                # Se verifica si la respuesta esta correcta y se le asigna el puntaje
                if Pregunta7 == Verdadero:
                    Puntaje += 1
                    print("Felicidades +1 punto, tu puntaje por el momento es de: ", Puntaje, " Puntos")
                else:
                    print("Que mal, Era verdadera, tu puntaje por el momento es de:", Puntaje, " Puntos")

                Pregunta8 = str(input("¿Python se puede usar para hacer paginas web?: "))  # True
                # Se verifica si la respuesta esta correcta y se le asigna el puntaje
                if Pregunta8 == Verdadero:
                    Puntaje += 1
                    print("Felicidades +1 punto, tu puntaje por el momento es de: ", Puntaje, " Puntos")
                else:
                    print("Que mal, Era verdadera, tu puntaje por el momento es de: ", Puntaje, " Puntos")

                Pregunta9 = str(input("¿La funcion str convierte los caracteres a numeros?: "))  # False
                # Se verifica si la respuesta esta correcta y se le asigna el puntaje
                if Pregunta9 == Falso:
                    Puntaje += 1
                    print("Felicidades +1 punto, tu puntaje por el momento es de: ", Puntaje, " Puntos")
                else:
                    print("Que mal, Era Falsa, tu puntaje por el momento es de: ", Puntaje, " Puntos")

                Pregunta10 = str(input("¿Para imprimir texto en consola se puede usar la funcion input?: "))  # False
                # Se verifica si la respuesta esta correcta y se le asigna el puntaje
                if Pregunta10 == Falso:
                    Puntaje += 1
                    print("Felicidades +1 punto, tu puntaje por el momento es de: ", Puntaje, " Puntos")
                else:
                    print("Que mal, Era Falsa, tu puntaje por el momento es de: ", Puntaje, " Puntos")

                if Puntaje == 0:
                    print("¿Encerio fui el único que se leyó los documentos?, tu puntaje fue de: ", Puntaje, " Puntos")
                elif Puntaje == 1:
                    print("Deberías estudiar mas, tu puntaje fue de: ", Puntaje, " Puntos")
                elif Puntaje == 2:
                    print("mmm creo que no te gusta la lectura, tu puntaje fue de: ", Puntaje, " Puntos")
                elif Puntaje == 3:
                    print("¿Hiciste todo al bateo verdad?, tu puntaje fue de: ", Puntaje, " Puntos")
                elif Puntaje == 4:
                    print("Wueno, ¿prestaste atención en clase?, tu puntaje fue de: ", Puntaje, " Puntos")
                elif Puntaje == 5:
                    print("Comienza a ser aceptable, tu puntaje fue de: ", Puntaje, " Puntos")
                elif Puntaje == 6:
                    print("Aceptable")
                elif Puntaje == 7:
                    print("Tu si prestaste atencion :v, tu puntaje fue de: ", Puntaje, " Puntos")
                elif Puntaje == 8:
                    print("Me agradas, tu puntaje fue de: ", Puntaje, " Puntos")
                elif Puntaje == 9:
                    print("¿Mmmm estaban sencillas verdad?, tu puntaje fue de: ", Puntaje, " Puntos")
                else:
                    print("Las preguntas estaban super sencillas, has ganado, gracias por jugar mi juego :), tu puntaje fue de: ", Puntaje)

            if NumPro2 == 0:
                print("Saliendo, hasta pronto gracias por venir ˄˄")
                break
            else:
                print('No has seleccionado una opcion disponible, por favor seleccione una de las opciones disponibles')

    elif NumPro0 == 3:
        print("Saliendo, hasta pronto gracias por venir ˄˄")
        break

    else:
        print("Gracias por usar este programa ;)")
