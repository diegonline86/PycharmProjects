__author__ = 'Diego Alberto Silguero'
# -*- coding: utf-8 -*-
class Persona():
    def __init__(self,  nombre, apellidos, edad):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__edad = edad

    @property
    def nombre(self):
        return  self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    def __str__(self):
        return self.__apellidos+", "+self.__nombre+"\t - "+str(self.__edad)+" años"

    def __gt__(self, other):
        #A igualdad de apellidos
        if(self.__apellidos == other.apellidos):
            #desempate por edad
            return self.__edad > other.edad
        else:
            #En caso contrario orden lexicográfico ascendente por apellidos
            return self.__apellidos > other.apellidos


list_personas = list()

list_personas.append(Persona("Diego Alberto","Silguero",29))
list_personas.append(Persona("Luis Miguel","López Magaña",33))
list_personas.append(Persona("Marta","Sánchez Pérez",21))
list_personas.append(Persona("Antonio","Llopis Pérez",35))
list_personas.append(Persona("Maria","Fuentes Gallardo",22))
list_personas.append(Persona("José Antonio","López López",45))
list_personas.append(Persona("José Maria","Llopis Pérez",22))

print("Lista NO ordenada"
      "\n--------------------------------------")
#Imprimimos la lista no orenada
for p in list_personas:
    print(p)

print("\nLista ordenada por apellidos y/o edad"
      "\n--------------------------------------")
list_personas.sort()
#Imprimimos la lista no orenada
for p in list_personas:
    print(p)
