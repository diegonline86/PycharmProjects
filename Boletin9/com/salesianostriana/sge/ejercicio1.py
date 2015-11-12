__author__ = 'Diego Alberto Silguero'
# -*- coding: utf-8 -*-
fich = open("datos_ficheros.txt","r")

print(fich.name)
print("Longitud de la primera linea: ",len(fich.readline()))