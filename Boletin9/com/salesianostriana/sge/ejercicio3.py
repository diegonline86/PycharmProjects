__author__ = 'Diego Alberto Silguero'
# -*- coding: utf-8 -*-
fich = open("datos_ficheros.txt","r")
linea = fich.readline()
#usando el método split separamos los enteros delimitados por espacios y los guardamos en una lista
enteros = linea.split()

print("Número de enteros en primera linea: ",len(enteros))


