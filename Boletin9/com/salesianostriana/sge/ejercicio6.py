# -*- coding: utf-8 -*-
fich = open("datos_ficheros.txt","r")

lineas = fich.readlines()
tam = len(lineas)
ultima_linea = lineas[tam-2].replace("\n","").strip()


print(ultima_linea)

#print("Producto de la ultima linea: ",sum(map(int,ultima_linea)))
