__author__ = 'Diego Alberto Silguero'
# -*- coding: utf-8 -*-
fich = open("datos_ficheros.txt","r")
fich_res = open("res_suma.txt","w+")
suma = 0
linea = fich.readline()
#usando el método split separamos los enteros delimitados por espacios y los guardamos en una lista
enteros = linea.split()

for n in enteros:
    suma += int(n)

fich_res.write("La suma de todos los números de la primera linea es: "+str(suma))