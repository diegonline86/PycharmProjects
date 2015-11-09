__author__ = 'Diego Alberto Silguero'
# -*- coding: utf-8 -*-
import operator

votos = dict()
nombre = ""

while(nombre != "FIN"):
    nombre = input("Introduce nombre: ")
    if(nombre != "FIN"):
        cantidad = int(input("Cantidad de votos: "))
        votos[nombre]=cantidad

#mostramos una representacion del dictionary ordenado por valores de manera descendente
print("\nResultados de la votación"
      "\n------------------------")
print(sorted(votos.items(), key = operator.itemgetter(1), reverse= True))
#imprimimos al más votado
print("\nGanador"
      "\n---------")
print(max(sorted(votos.items(), key = operator.itemgetter(1), reverse= True)))
