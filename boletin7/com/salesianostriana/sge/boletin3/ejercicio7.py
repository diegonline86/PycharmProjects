__author__ = 'Diego Alberto Silguero'
# -*- coding: utf-8 -*-

class Nota():
    id = 1
    def __init__(self, asunto):
        self.__id_nota = id
        self.__asunto = asunto
        self.id =+ 1

    @property
    def id_nota(self):
        return self.__id_nota

    @id_nota.setter
    def id_nota(self, id):
        self.__id_nota = id

    @property
    def asunto(self):
        return self.__asunto

    @asunto.setter
    def asunto(self, asunto):
        self.__asunto = asunto

    def __str__(self):
        return str(self.__id_nota)+" - "+self.__asunto


def menu(agenda):
    opcion= int(input("AGENDA\n"
          "1. Agregar nota\n"
          "2. Borrar nota\n"
          "3. Mostrar una nota\n"
          "4. Mostrar todas las notas\n"
          "0. Salir\n\n"
          "Elige opcion: "))

    if(opcion == 1):
        nota = input("Escribe tu nota: ")
        list(agenda).append(Nota(nota))
        menu(agenda)
    elif(opcion == 2):
        nota = int(input("Introduce número de nota: "))
        list(agenda).remove(nota-1)
        menu(agenda)
    elif(opcion == 3):
        nota = int(input("Introduce número de nota: "))
        list(agenda).__getitem__(nota-1)
        menu(agenda)
    elif(opcion!=0):
        menu(agenda)


agenda = list()
menu(agenda)







