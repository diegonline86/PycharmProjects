__author__ = 'Diego Alberto Silguero'
# -*- coding: utf-8 -*-
votos = dict()
nombre = ""

while(nombre != "FIN"):
    if(nombre != "FIN"):
        nombre = input("Introduce nombre: ")
        cantidad = int(input("Cantidad de votos: "))
        votos[nombre]=cantidad

print(votos)


