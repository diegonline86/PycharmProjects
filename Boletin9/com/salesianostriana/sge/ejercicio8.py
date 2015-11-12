__author__ = 'Diego Alberto Silguero'
# -*- coding: utf-8 -*-
fich = open("con_comentarios.txt")
cont = 0
linea = fich.readline()

while(linea != ""):
    if(linea.startswith("#") == False):
        cont += 1
    linea = fich.readline()

print("El número de lineas no comentadas es ",cont)