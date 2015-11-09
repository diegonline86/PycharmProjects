# -*- coding: utf-8 -*-
from com.salesianostriana.sge.cifrado_cesar.utiles_cifrado import *

fich = open("amistad.txt","w+")
fich_enc = open("amistad_enc.txt","w+")

def leer_fichero(fich):
    contenido = fich.readline();
    while (contenido != ""):
        print(contenido,end="")
        contenido = fich.readline();

def encriptar_fichero(fich):
    contenido = fich.readline();
    while (contenido != ""):
        fich_enc.write(encriptar(3,contenido))
        contenido = fich.readline();

def desencriptar_fichero(fich):
    contenido = fich.readline();
    while (contenido != ""):
        fich_enc.write(desencriptar(3,contenido))
        contenido = fich.readline();

desencriptar_fichero(fich_enc)



