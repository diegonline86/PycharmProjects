__author__ = 'Diego Alberto Silguero'
# -*- coding: utf-8 -*-
fich = open("datos_ficheros.txt","r")

print(fich.name)
cont = 1
linea = fich.readline()

while(linea != ""):
    cont += 1
    linea = fich.readline()

print("Numero de lineas: ",cont)