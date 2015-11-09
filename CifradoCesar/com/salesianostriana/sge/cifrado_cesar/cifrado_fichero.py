# -*- coding: utf-8 -*-
from com.salesianostriana.sge.cifrado_cesar.utiles_cifrado import *

list_fich = list()
list_fich.append(open("amistad.txt","r+"))
list_fich.append(open("las_apariencias.txt","r+"))


opcion = -1

def leer_fichero(fich):
    contenido = fich.readline();
    while (contenido != ""):
        print(contenido,end="")
        contenido = fich.readline();

def encriptar_fichero(fich):
    fich_enc = open("fich_enc.txt","w+")

    #procesamos el contenido del fichero orginal encriptandolo
    #y guardando el resultado en un fichero auxiliar
    contenido = fich.readline();
    while (contenido != ""):
        fich_enc.write(encriptar(3,contenido))
        contenido = fich.readline();

    # finalmente sobreescribimos el fichero original
    contenido = fich_enc.readline();
    while (contenido != ""):
        fich.write(contenido)
        contenido = fich.readline();

    #cerramos el flujo del fichero auxiliar
    fich_enc.close()
    #eliminamos el fichero auxiliar
    del fich_enc

def desencriptar_fichero(fich):
    fich_enc = open("fich_enc.txt","w+")

    #procesamos el contenido del fichero orginal desencriptandolo
    #y guardando el resultado en un fichero auxiliar
    contenido = fich.readline();
    while (contenido != ""):
        fich_enc.write(desencriptar(3,contenido)+"\n")
        contenido = fich_enc.readline();

    # finalmente sobreescribimos el fichero original
    contenido = fich_enc.readline();
    while (contenido != ""):
        fich.write(contenido)
        contenido = fich.readline();

    #cerramos el flujo del fichero auxiliar
    fich_enc.close()
    #eliminamos el fichero auxiliar
    del fich_enc

while(opcion != 0):
    opcion = int(input("\nOPCIONES"
                       "\n---------"
                       "\n1. Encriptar fichero"
                       "\n2. Desencriptar fichero"
                       "\n3. Leer fichero"
                       "\n0. Salir"
                       "\n\nElige opcion: "))

    if(opcion == 1):
        for f in list_fich:
            print(list_fich.index(f)+1," - ",f.name)
        f = int(input("Elige fichero: "))
        if(f < 1 or f > len(list_fich)):
            print("ERROR. El fichero no existe")
        else:
            encriptar_fichero(list_fich[f-1])
    if(opcion == 2):
        for f in list_fich:
            print(list_fich.index(f)+1," - ",f.name)
        f = int(input("Elige fichero: "))
        if(f < 1 or f > len(list_fich)):
            print("ERROR. El fichero no existe")
        else:
            desencriptar_fichero(list_fich[f-1])
    if(opcion == 3):
        for f in list_fich:
            print(list_fich.index(f)+1," - ",f.name)
        f = int(input("Elige fichero: "))
        if(f < 1 or f > len(list_fich)):
            print("ERROR. El fichero no existe")
        else:
            leer_fichero(list_fich[f-1])


#cerramos el flujo de todos los ficheros
for i in range(0,len(list_fich)):
    list_fich[i].close()






