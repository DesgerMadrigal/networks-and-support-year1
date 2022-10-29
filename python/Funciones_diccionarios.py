#!/usr/bin/env python3
# -*- encode: utf-8 -*-

#funciones basicas agregar, eliminar y ver

def agregar_usuario():
    global usuarios
    id = int(input("ingrese el ID: "))
    nombre = input("ingrese nombre: ")
    direct = input("ingrese direccion: ")
    tel = int(input("ingrese su tel: "))
    usuarios[id] = nombre, direct, tel
    print(usuarios)

def delete(id):
    global usuarios
    del(usuarios[id])
    print("Eliminado")

def listar():
    global usuarios
    for user in usuarios:
        print(
    """
    ID: {}
    Nombre: {}
    Direccion: {}
    Tel: {}
    """.format(user, usuarios[user][0], usuarios[user][1], usuarios[user][2]))

#diccionarios a usar en cada modulo
usuarios = {}

while True:
    print("----Aplicacion en python----\n")
    print("[1]--------Agregar----------\n")
    print("[2]--------eliminar---------\n")
    print("[3]--------listar-----------\n")
    print("[4]--------salir------------\n ")


    option = int(input("selecciona una opcion: "))
    if option == 1:
        agregar_usuario()
    elif option == 2:
        id = int(input("Ingrese el Id del usuario: "))
        delete(id)
    elif option == 3:
            listar()
    elif option == 4:
        break

