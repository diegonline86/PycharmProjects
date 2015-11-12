__author__ = 'Diego Alberto Silguero'
# -*- coding: utf-8 -*-
fich = open("datos_ficheros.txt","r")
enteros = fich.read().split()
suma = 0

for n in enteros:
    if(int(n)%2 != 0):
        suma += int(n)

print("La suma de todos los impares es: ",suma)