# -*- coding: utf-8 -*-

def encriptar(llave,texto):
    res = ""
    for i in range(0,len(texto)):
        res += chr(ord(texto[i])+llave)

    return res

def desencriptar(llave,texto):
    res = ""
    for i in range(0,len(texto)):
        res += chr(ord(texto[i])-llave)

    return res

opcion = -1
texto = ""

while(opcion != 0):
    opcion = int(input("\nOPCIONES"
                       "\n--------"
                       "\n1. Encriptar texto"
                       "\n2. Desencriptar texto"
                       "\n0. Salir"
                       "\n\nElige opcion: "))
    if opcion == 1:
        texto = input("Escribe el texto: ")
        llave = int(input("Introduce la llave (1-26): "))
        texto = encriptar(llave,texto)
        print("Resultado: ",texto)
    elif opcion == 2:
        llave = int(input("Introduce la llave (1-26): "))
        texto = desencriptar(llave,texto)
        print("Resultado: ",texto)

